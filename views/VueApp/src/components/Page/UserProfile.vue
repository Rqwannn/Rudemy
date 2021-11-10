<template>
    <div>
        <Navbar></Navbar>

        <main class="profile my-md">
            <div class="container">
                <div class="layout">
                    <div class="column column--1of3">
                    <div class="card text-center">
                        <div class="card__body dev">
                            <img class="avatar avatar--xl" :src="Path + '' + Data.profile_image" />
                            <h2 class="dev__name">{{Data.name}}</h2>
                            <p class="dev__title">{{Data.short_intro}}</p>
                            <p class="dev__location">Based In {{Data.location}}</p>
                            <router-link :to="{name:'Message_Form', params: {id: Data.id}}" v-if="Data.id != Profile.id" style="margin-top: 10px;" class="btn btn--sub btn--lg">
                                Send Message 
                            </router-link>
                        </div>
                    </div>
                    </div>
                    <div class="column column--2of3">
                    <div class="devInfo">
                        <h3 class="devInfo__title">About Me</h3>
                        <p class="devInfo__about">
                            {{Data.bio}}
                        </p>
                    </div>
                    <div class="devInfo">
                        <h3 class="devInfo__title">Skills</h3>
                        <div class="devInfo__skills">                                
                            <div class="devInfo__otherSkills">
                                <span v-for="result in Data.skill" :key="result.id" class="tag tag--pill tag--sub tag--lg">
                                    <small>{{ result.name }}</small>
                                </span>
                            </div>
                        </div>
                    </div>
                    <div class="devInfo">
                        <h3 class="devInfo__title">Course</h3>
                            <div class="grid grid--two">

                                <div class="column" v-for="result in Data.course_set" :key="result.id">
                                    <div class="card project">
                                    <a href="#" class="project">
                                        <img class="project__thumbnail" :src="Path + '' + result.featured_image" alt="project thumbnail" />
                                        <div class="card__body">
                                        <h3 class="project__title">{{ result.title }}</h3>
                                        <p><a class="project__author" href="profile.html">By owner {{ result.owner.name }}</a></p>
                                        <p class="project--rating">
                                            <span style="font-weight: bold;">{{ result.vote_ratio }} %</span> Postitive
                                            Feedback ({{ result.total }} Vote {{ result.vote_total > 0 ? 's' : '' }})
                                        </p>
                                            <div class="project__tags">
                                                <span v-for="items in result.tags" :key="items.id" class="tag tag--pill tag--main">
                                                    <small>{{ items.name }}</small>
                                                </span>
                                            </div>
                                        </div>
                                    </a>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import NavBar from '../Template/Navbar'
import { axios } from '../../axios-api'
import { URL } from '../../ApiBaseUrl'

export default {
    data(){
        return {
            Data: [],
            Profile: [],
            Path: URL
        }
    },
    components:{
        'Navbar': NavBar
    },
    created(){
        axios.get(`/api/getUser/${this.$route.params.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => {
            this.Data = response.data.data;
            this.Profile = response.data.profile;
        })
        .catch(err => {
          console.log(err)
        })
    }
}
</script>