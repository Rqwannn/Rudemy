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
                    class="avatar avatar--xl dev__avatar"
                    :src="Path + '' + DataProfile.profile_image"
                    />
                    <h2 class="dev__name">{{ DataProfile.name }}</h2>
                    <p class="dev__title">{{ DataProfile.short_intro }}</p>
                    <p class="dev__location">Based In {{ DataProfile.location }}</p>
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
                <a
                    class="tag tag--pill tag--sub settings__btn tag--lg"
                    href="#"
                    ><i class="im im-plus"></i> Add Skill</a
                >
                </div>

                <table class="settings__table">
                    <tr v-for="result in DataProfile.skill" :key="result.id">
                        <td class="settings__tableInfo">
                        <h4>{{ result.name }}</h4>
                        </td>
                        <td class="settings__tableActions">
                        <a
                            class="tag tag--pill tag--main settings__btn"
                            href="#"
                            ><i class="im im-edit"></i> Edit</a
                        >
                        <a
                            class="tag tag--pill tag--main settings__btn"
                            href="#"
                            ><i class="im im-x-mark-circle-o"></i> Delete</a
                        >
                        </td>
                    </tr>
                </table>

                <div class="settings">
                <h3 class="settings__title">Course</h3>
                <a
                    class="tag tag--pill tag--sub settings__btn tag--lg"
                    href="#"
                    ><i class="im im-plus"></i> Add Course</a
                >
                </div>

                <table class="settings__table">
                    <tr v-for="result in DataProfile.course_set" :key="result.id">
                        <td class="settings__thumbnail">
                        <a href="#"
                            ><img :src="Path + '' + result.featured_image" alt="Project Thumbnail"
                        /></a>
                        </td>
                        <td class="settings__tableInfo">
                        <a href="#">{{ result.title }}</a>
                        <p>{{ result.description }}</p>
                        </td>
                        <td class="settings__tableActions">
                        <a
                            class="tag tag--pill tag--main settings__btn"
                            href="#"
                            ><i class="im im-edit"></i> Edit</a
                        >
                        <a
                            class="tag tag--pill tag--main settings__btn"
                            href="#"
                            ><i class="im im-x-mark-circle-o"></i> Delete</a
                        >
                        </td>
                    </tr>
                </table>
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
        axios.get(`api/profileUser/${this.$store.state.UserData.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then( response => {
                this.DataProfile = response.data;
            }).catch( err => {
                console.log(err)
            });
    }
}
</script>