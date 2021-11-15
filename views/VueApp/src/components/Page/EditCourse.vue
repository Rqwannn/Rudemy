<template>
    <div>
        <main class="formPage my-xl">
            <div class="content-box">
                <div class="formWrapper">
                    <router-link class="backButton" :to="{name:'Account'}">
                            <span style="font-size: 20px;">&#8592;</span>
                    </router-link>
                <br />

                <form @submit.prevent="Submit()">

                    <div class="form__field">
                        <label>Title: </label>
                        <input type="text" class="input" placeholder="Title..." v-model="ProjectTitle">
                    </div>

                    <div class="form__field">
                        <label>Project Image: </label>
                        <input type="file" class="input" accept="image/png, image/jpeg, image/jpg" @change="Upload($event)">
                        <img :src="PreviewImg" v-if="PreviewImg != ''" class="ml-3" style="width: 100px;">
                    </div>

                    <div class="form__field">
                        <label>Old Image: </label>
                        <img :src="Path + OldImage" v-if="OldImage != ''" class="ml-3" style="width: 100px;">
                    </div>

                    <div class="form__field">
                        <label>Description: </label>
                        <input type="text" class="input" placeholder="Description..." v-model="Description">
                    </div>

                    <div class="form__field">
                        <label>Demo Link: </label>
                        <input type="text" class="input" placeholder="Demo Link..." v-model="Demo_Link">
                    </div>

                    <div class="form__field">
                        <label>Source Link: </label>
                        <input type="text" class="input" placeholder="Source Link..." v-model="Source_Link">
                    </div>

                    <div class="form__field">
                        <div v-for="result in Tags" :key="result.id"
                            class="project-tag tag tag--pill tag--main"
                            :data-tag="result.id"
                            @click="DeleteTags($event)"
                            :data-course="ProjecID">
                            {{result.name}} &#215;
                        </div>
                    </div>

                    <div class="form__field">
                        <label for="formInput#text">New Tags: </label>
                        <textarea
                            name="newtags"
                            class="input"
                            placeholder="Tags..."
                            style="resize: none"
                            v-model="NewTags"
                        ></textarea>
                    </div>

                    <input
                    class="btn btn--sub btn--lg my-md"
                    type="submit"
                    value="Submit"
                    />
                </form>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import { axios } from '../../axios-api'
import { URL as BaseURL } from '../../ApiBaseUrl'

export default {
    data(){
        return {
            Data: [],
            ProjectTitle: "",
            Featured_Image: null,
            Description: "",
            Demo_Link: "",
            Source_Link: "",
            Tags: [],
            NewTags: "",
            PreviewImg: "",
            OldImage: "",
            ProjecID: "",
            Path: BaseURL,
        }
    },
    props: ['id'],
    created(){
        this.getData()
    },
    methods: {
        getData(){
            axios.get(`/api/getCourse/${this.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then(response => {
                this.ProjectTitle = response.data.data.title
                this.Description = response.data.data.description
                this.Demo_Link = response.data.data.demo_link
                this.Source_Link = response.data.data.source_link
                this.OldImage = response.data.data.featured_image
                this.Tags = response.data.data.tags
                this.ProjecID = response.data.data.id
            })
            .catch(err => {
                console.log(err)
            })
        },
        Upload (e){
            this.PreviewImg = URL.createObjectURL(e.target.files[0]);
            this.Featured_Image = e.target.files[0];

            const blob = this.Featured_Image.slice(0, this.Featured_Image.size, `${this.Featured_Image.type}`);
            let changeName = `${this.Featured_Image.name.split('.')[0]}-`;

            for(let i = 0; i < 20; i++){
                let setNumber = Math.floor(Math.random() * (18 - 0 + 1)) + 0;
                let random = 'Uysx1Ms6HfaiAZ23Oe3';
                changeName += random[setNumber];
            }

            const newFile = new File([blob], `${changeName}.${this.Featured_Image.name.split('.').at(-1)}`, {type: `${this.Featured_Image.type}`});
            this.Featured_Image = newFile
        },
        DeleteTags: function(e){
            this.$swal({
                title: 'Attention',
                text: `Are you sure want to delete this tags?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes'
            }).then((result) => {
                if (result.isConfirmed) {
                    const TagID = e.target.dataset.tag;
                    const CourseID = e.target.dataset.course;

                    axios.delete(`/api/deleteCourseTag/${TagID}/${CourseID}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                    .then( response => {
                        if(response.data.status){
                            this.$swal({
                                title: 'Success',
                                text: `${response.data.message}`,
                                icon: 'success',
                                showCancelButton: false,
                                confirmButtonColor: '#3085d6',
                                confirmButtonText: 'Ok'
                            }).then((result) => {
                                if (result.isConfirmed) {
                                    this.getData()
                                }
                            })
                        } else {
                            this.$swal({
                                icon: 'error',
                                title: 'Oops...',
                                text: `${response.data.message}`,
                            })
                        }
                    })
                    .catch( err => console.log(err))
                }
            })
        },
        Submit: function(){
            if(this.ProjectTitle == "" || this.Description == "" || this.Demo_Link == "" || this.Source_Link == ""){
                this.$swal({
                    icon: 'warning',
                    title: 'Attention',
                    text: `All inputs are mandatory`,
                })
            } else {
                const SetWrapper = new FormData()

                SetWrapper.append('title', this.ProjectTitle);
                SetWrapper.append('description', this.Description);
                SetWrapper.append('demo_link', this.Demo_Link);
                SetWrapper.append('source_link', this.Source_Link);
                SetWrapper.append('idProject', this.ProjecID);
                
                if(this.NewTags.length > 0){
                    SetWrapper.append('newtags', this.NewTags);
                }

                if(this.Featured_Image != null){
                    SetWrapper.append('featured_image', this.Featured_Image);
                }

                axios.put('/api/editCourse/', SetWrapper, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then( response => {
                    if(response.data.status){
                        this.$swal({
                            title: 'Success',
                            text: `${response.data.message}`,
                            icon: 'success',
                            showCancelButton: false,
                            confirmButtonColor: '#3085d6',
                            confirmButtonText: 'Ok'
                        }).then((result) => {
                            if (result.isConfirmed) {
                                this.$router.push({name:'Account'}).catch(() => {

                                });
                            }
                        })
                    } else {
                        this.$swal({
                            icon: 'error',
                            title: 'Oops...',
                            text: `${response.data.message}`,
                        })
                    }
                })
                .catch( err => console.log(err))
            }
        }
    }
}
</script>