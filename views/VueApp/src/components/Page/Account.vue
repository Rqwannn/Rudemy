<template>
    <div>
      <Navbar></Navbar>

      <main class="settingsPage profile my-md">
        <div class="container">
            <div class="layout">
            <div class="column column--1of3">
                <div class="card text-center">
                    <div class="card__body dev">
                        <router-link class="tag tag--pill tag--main settings__btn" :to="{name:'EditUser', params: {id : DataProfile.id}}">
                            <i class="im im-edit"></i> Edit
                        </router-link>
                        <img
                            @click="ChangeImg()"
                            style="cursor: pointer;"
                            class="avatar avatar--xl dev__avatar"
                            :src="Path + '' + DataProfile.profile_image"
                        />
                        <h2 class="dev__name">{{ DataProfile.name }}</h2>
                        <p class="dev__title">{{ DataProfile.short_intro }}</p>
                        <p class="dev__location">Based In {{ DataProfile.location }}</p>
                        <input type="file" style="display: none;" @change="Upload($event)" accept="image/png, image/jpeg, image/jpg" class="UploadProfileIMG">
                    </div>
                </div>
            </div>
            <div class="column column--2of3">
                <div class="devInfo">
                    <h3 class="devInfo__title">About Me</h3>
                    <p class="devInfo__about">{{ DataProfile.bio }}</p>
                </div>
                <div class="settings">
                    <h3 class="settings__title">Skills</h3>
                    <router-link class="tag tag--pill tag--sub settings__btn tag--lg" :to="{name:'TambahSkill'}">
                        <i class="im im-plus"></i> Add Skill
                    </router-link>
                </div>

                <table class="settings__table">
                    <tr v-for="result in DataProfile.skill" :key="result.id">
                        <td class="settings__tableInfo">
                            <h4>{{ result.name }}</h4>
                        </td>
                        <td class="settings__tableActions">
                            <a class="tag tag--pill tag--main settings__btn" href="#" @click.prevent="DeleteSkill(result.id)">
                                <i class="im im-x-mark-circle-o"></i> Delete
                            </a>
                        </td>
                    </tr>
                </table>

                <div class="settings" v-if="DataProfile.status == 1">
                    <h3 class="settings__title">Course</h3>
                    <router-link class="tag tag--pill tag--sub settings__btn tag--lg" :to="{name:'TambahCourse'}">
                        <i class="im im-plus"></i> Add Course
                    </router-link>
                </div>

                <table class="settings__table" v-if="DataProfile.status == 1">
                    <tr v-for="result in DataProfile.course_set" :key="result.id">
                        <td class="settings__thumbnail">
                            <router-link :to="{name:'UserCourse', params: {id: result.id}}">
                                <img :src="Path + '' + result.featured_image" alt="Project Thumbnail"/>
                            </router-link>
                        </td>
                        <td class="settings__tableInfo">
                            <router-link :to="{name:'UserCourse', params: {id: result.id}}">
                                {{ result.title }}
                            </router-link>
                            <p>{{ result.description }}</p>
                        </td>
                        <td class="settings__tableActions">
                        <router-link :to="{name:'EditCourse', params: {id: result.id}}" class="tag tag--pill tag--main settings__btn" >
                            <i class="im im-edit"></i> Edit
                        </router-link>
                        <a
                            @click.prevent="DeleteCourse(result.id)"
                            class="tag tag--pill tag--main settings__btn"
                            href=""
                            ><i class="im im-x-mark-circle-o"></i> Delete</a
                        >
                        </td>
                    </tr>
                </table>
                <p v-else>Your status is still a participant, <a href="/" @click.prevent="BecomeTeach()">do you want to teach?</a></p>
            </div>
            </div>
        </div>
        </main>
    </div>
</template>

<script>
import NavBar from '../Template/Navbar'
import { mapState } from 'vuex'
import { axios } from '../../axios-api'
import { URL } from '../../ApiBaseUrl'

export default {
    data(){
        return {
            Title: 'Account | Rudemy',
            DataProfile: [],
            Path: URL,
            ProfileImg: null
        }
    },
    components: {
      'Navbar': NavBar,
    },
    computed: mapState(['UserData']),
    watch: {
      title: {
        immediate: true,
          handler() {
            document.title = this.Title;
            this.$store.commit('setPath', { path: this.$route.fullPath })
          }
        },
    },
    created(){
        this.getData();
    },
    methods:{
        Upload (e){
            this.ProfileImg = e.target.files[0]
            const blob = this.ProfileImg.slice(0, this.ProfileImg.size, `${this.ProfileImg.type}`);
            let changeName = `${this.ProfileImg.name.split('.')[0]}-`;

            for(let i = 0; i < 20; i++){
                let setNumber = Math.floor(Math.random() * (18 - 0 + 1)) + 0;
                let random = 'LksS9Ms5H6aiAB23Oe3';
                changeName += random[setNumber];
            }

            const newFile = new File([blob], `${changeName}.${this.ProfileImg.name.split('.').at(-1)}`, {type: `${this.ProfileImg.type}`});
            this.ProfileImg = newFile

            if(this.ProfileImg == null){
                this.$swal({
                    icon: 'error',
                    title: 'Oppss...',
                    text: `Profile picture failed to change`,
                })
            } else {
                if(this.ProfileImg.size >= 1500000){
                    this.$swal({
                        icon: 'error',
                        title: 'Oppss...',
                        text: `Image cannot be more than 1.5 MB`,
                    })
                } else {
                    const WrapperData = new FormData()
                    WrapperData.append('profile_image', this.ProfileImg)

                    axios.put('/api/UpdateProfileImg/', WrapperData, { 
                        headers: { 
                            Authorization: `Bearer ${this.$store.state.accessToken}`,
                            'Content-Type': 'multipart/form-data'
                        } 
                    })
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
                                this.getData();
                            })
                        } else {
                            this.$swal({
                                icon: 'error',
                                title: 'Oops...',
                                text: `${response.data.message}`,
                            })
                        }
                    })
                    .catch( err => console.log(err) )
                }
            }
        },
        DeleteSkill: function(e){
            this.$swal({
                title: 'Attention',
                text: `Are you sure you want to delete this skill?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes'
            }).then((result) => {
                if (result.isConfirmed) {
                    axios.delete(`api/DeleteSkill/${e}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
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
                                this.getData();
                            })
                        } else {
                            this.$swal({
                                icon: 'error',
                                title: 'Oops...',
                                text: `${response.data.message}`,
                            })
                        }
                    }).catch( err => {
                        console.log(err)
                    });
                }
            })
        },
        getData: function(){
            axios.get(`api/profileUser/${this.$store.state.UserData.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then( response => {
                this.DataProfile = response.data;
            }).catch( err => {
                console.log(err)
            });
        },
        ChangeImg: function(){
            this.$swal({
                title: 'Attention',
                text: `Do you want to change your profile image?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes'
            }).then((result) => {
                if (result.isConfirmed) {
                    const UploadProfileIMG = document.querySelector('.UploadProfileIMG');
                    UploadProfileIMG.click()
                }
            })
        },
        DeleteCourse: function(e){
            this.$swal({
                title: 'Attention',
                text: `Are you sure you want to delete this course?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes'
            }).then((result) => {
                if (result.isConfirmed) {
                    axios.delete(`/api/deleteCourse/${e}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                    .then(response => {
                        if(response.data.status){
                            this.$swal({
                                title: 'Success',
                                text: `${response.data.message}`,
                                icon: 'success',
                                showCancelButton: false,
                                confirmButtonColor: '#3085d6',
                                confirmButtonText: 'Ok'
                            }).then((result) => {
                                this.getData();
                            })
                        } else {
                            this.$swal({
                                icon: 'error',
                                title: 'Oops...',
                                text: `${response.data.message}`,
                            })
                        }
                    })
                    .catch( err => console.log(err) )
                }
            })
        },
        BecomeTeach: function(){
            this.$swal({
                title: 'Attention',
                text: `Are you sure?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes'
            }).then((result) => {
                if (result.isConfirmed) {
                    axios.put('/api/UpdateStatusProfile/', {'status': 1},{ headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
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
                                this.getData();
                            })
                        } else {
                            this.$swal({
                                icon: 'error',
                                title: 'Oops...',
                                text: `${response.data.message}`,
                            })
                        }
                    })
                    .catch( err => console.log(err) )
                }
            })
        }
    }
}
</script>