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
                    <input type="file" class="input" @change="Upload($event)">
                    <img :src="PreviewImg" v-if="PreviewImg != ''" class="ml-3" style="width: 100px;">
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
                    <label for="formInput#text">Tags: </label>
                    <textarea
                        name="newtags"
                        class="input"
                        placeholder="Tags..."
                        style="resize: none"
                        v-model="Tags"
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

export default {
    data(){
        return {
            Title: 'Insert Course | Rudemy',
            ProjectTitle: "",
            Featured_Image: null,
            Description: "",
            Demo_Link: "",
            Source_Link: "",
            Tags: "",
            PreviewImg: "",
        }
    },
    watch: {
      title: {
        immediate: true,
          handler() {
            document.title = this.Title;
            this.$store.commit('setPath', { path: this.$route.fullPath })
          }
        },
    },
    methods:{
        Upload (e){
            this.PreviewImg = URL.createObjectURL(e.target.files[0]);
            this.Featured_Image = e.target.files[0];
        },
        Submit: function(){
            if(this.ProjectTitle == "" || this.Featured_Image == null || this.Description == "" || this.Demo_Link == "" || this.Source_Link == "" || this.Tags == ""){
                this.$swal({
                    icon: 'warning',
                    title: 'Attention',
                    text: `All inputs are mandatory`,
                })
            } else {
                const SetWrapper = new FormData()

                SetWrapper.append('title', this.ProjectTitle);
                SetWrapper.append('featured_image', this.Featured_Image);
                SetWrapper.append('description', this.Description);
                SetWrapper.append('demo_link', this.Demo_Link);
                SetWrapper.append('source_link', this.Source_Link);
                SetWrapper.append('tags', this.Tags);

                axios.post('/api/insertCourse/', SetWrapper, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
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