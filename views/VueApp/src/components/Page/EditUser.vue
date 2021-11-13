<template>
    <div>
        <main class="formPage my-xl">
            <div class="content-box">
                <div class="formWrapper">
                <router-link class="backButton" :to="{name:'Account'}">
                     <span style="font-size: 20px;">&#8592;</span>
                </router-link>
                <br />

                    <form @submit.prevent="submitUpdate()">
                    
                        <div class="form__field">
                            <label>Name: </label>
                            <input type="text" class="input" v-model="Name" placeholder="Your Name">
                        </div>

                        <div class="form__field">
                            <label>Email: </label>
                            <input type="email" class="input" v-model="Email" placeholder="Your Email">
                        </div>

                        <div class="form__field">
                            <label>Username: </label>
                            <input type="text" class="input" v-model="Username" placeholder="Your Username">
                        </div>

                        <div class="form__field">
                            <label>Short Intro: </label>
                            <input type="text" class="input" v-model="Short_Intro" placeholder="Your Short Intro">
                        </div>

                        <div class="form__field">
                            <label>Location: </label>
                            <input type="text" class="input" v-model="Location" placeholder="Your Location">
                        </div>
                        
                        <div class="form__field">
                            <label>Bio: </label>
                            <textarea placeholder="Your Bio" class="input" v-model="Bio" style="resize: none;"></textarea>
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
import { URL } from '../../ApiBaseUrl'
import { axios } from '../../axios-api'

export default {
    props: ['id'],
    data(){
        return {
            Name: "",
            Email: "",
            Username: "",
            Location: "",
            Short_Intro: "",
            Bio: "",
            Title: "Developer | Rudemy",
            Path: URL
        }
    },
    created(){
        this.getData()
    },
    methods: {
        getData: function(){
            axios.get(`/api/getUser/${this.$route.params.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then(response => {
                this.Name = response.data.data.name;
                this.Email = response.data.data.user.email;
                this.Username = response.data.data.user.username;
                this.Location = response.data.data.location;
                this.Short_Intro = response.data.data.short_intro;
                this.Bio = response.data.data.bio;
            })
            .catch(err => {
                console.log(err)
            })
        },
        submitUpdate: function(){

            if(this.Name == '' || this.Email == '' || this.Username == '' || this.Location == '' || this.Short_Intro == '' || this.Bio == ''){
                this.$swal({
                    icon: 'warning',
                    title: 'Attention',
                    text: `All inputs are mandatory`,
                })
            } else {
                const WrapperData = new FormData()
                WrapperData.append('name', this.Name)
                WrapperData.append('email', this.Email)
                WrapperData.append('username', this.Username)
                WrapperData.append('location', this.Location)
                WrapperData.append('short_intro', this.Short_Intro)
                WrapperData.append('bio', this.Bio)

                const config = {
                    headers: {
                        "Accept" : "application/json",
                        "Authorization": `Bearer ${this.$store.state.accessToken}`,
                    }
                }

                axios.put('/api/editUser/', WrapperData, config).then( response => {
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
                }).catch( error => {
                    console.log(error);
                })
            }
        }
    },
    watch: {
        title: {
            immediate: true,
            handler() {
                document.title = this.Title;
            }
        },
    },
}
</script>