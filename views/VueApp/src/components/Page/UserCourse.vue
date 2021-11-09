<template>
    <div>
        <Navbar></Navbar>

        <main class="singleProject my-md">
            <div class="container">
            <div class="layout">
                <div class="column column--1of3">
                <h3 class="singleProject__subtitle">Tools & Stacks</h3>
                <div class="singleProject__toolStack">
                    <span v-for="result in Data.tags" :key="result.id" class="tag tag--pill tag--sub tag--lg">
                        <small>{{ result.name }}</small>
                    </span>
                </div>
                    <a v-if="Data.source_link" class="singleProject__liveLink" :href="Data.source_link" target="_blank">
                        <i class="im im-external-link"></i>Source Code
                    </a>
                    <a v-else-if="Data.demo_link" class="singleProject__liveLink" :href="Data.demo_link" target="_blank">
                        <i class="im im-external-link"></i>Live Demo
                    </a>
                </div>
                <div class="column column--2of3">
                <img class="singleProject__preview" :src="Path + '' + Data.featured_image" alt="portfolio thumbnail" />
                <a href="#" class="singleProject__developer">{{ NameOwner }}</a>
                <h2 class="singleProject__title">{{ Data.title }}</h2>
                <h3 class="singleProject__subtitle">About the Project</h3>
                <div class="singleProject__info">
                    {{ Data.description }}
                </div>

                <div class="comments">
                    <h3 class="singleProject__subtitle">Feedback</h3>
                    <h5 class="project--rating">
                    {{ Data.vote_ratio }} % Postitive Feedback ( {{ Data.vote_total }} Vote{{ Data.vote_total > 0 ? 's' : '' }})
                    </h5>

                    <p v-if="Warning">{{ Warning }}</p>
                    <p v-if="Profile.id == OwnerID">You cannot review your own work</p>
                    <form v-else-if="is_authenticated" @submit.prevent="SendComment()" class="form">

                        <div class="form__field">
                            <div style="display: flex; align-items: center;">
                                <p for="vote">Up: </p>
                                <input type="radio" @click="SetVote($event)" id="vote" class="input" name="vote" value="up" style="resize: none; cursor: pointer;">
                            </div>
                            <div style="display: flex; align-items: center;">
                                <p for="vote">Down: </p>
                                <input type="radio" @click="SetVote($event)" id="vote" class="input" name="vote" value="down" style="resize: none; cursor: pointer;">
                            </div>
                        </div>

                        <div class="form__field">
                            <p for="formInput#textarea">Body: </p>
                            <textarea class="input" style="resize: none;" v-model="body"></textarea>
                        </div>
                        
                        <input class="btn btn--sub btn--lg" type="submit" value="Comments" />
                    
                    </form>
                    <a v-else href="#">Please Login</a>

                    <div class="commentList">
                        <div v-for="review in CommentList" :key="review.id" class="comment">
                            <a href="#">
                            <img class="avatar avatar--md"
                                :src="Path + '' + review.owner.profile_image" alt="user" />
                            </a>
                            <div class="comment__details">
                            <a href="#" class="comment__author">{{ review.owner.name }}</a>
                            <p class="comment__info">
                                {{review.body}}
                            </p>
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
import { axios } from '../../axios-api'
import NavBar from '../Template/Navbar'
import { URL } from '../../ApiBaseUrl'

export default {
    data(){
        return {
            Data: [],
            Profile: [],
            Path: URL,
            is_authenticated: false,
            NameOwner: "",
            OwnerID: 0,
            body: '',
            Vote: '',
            Warning: ''
        }
    },
    computed: {
        CommentList: function(){
            let Wrapper = [];
            this.Data.review_set.forEach( result => {
                if(result.body != ''){
                    Wrapper.push(result);
                }
            })
            return Wrapper;
        }
    },
    components:{
        'Navbar': NavBar
    },
    created(){
        this.getData()
    },
    methods: {
        SendComment: function() {
            if(this.Vote == '' || this.body == ''){
                this.Warning = 'fill in the comment field first';
            } else {
                axios.post(`/api/insertReview/`, { id: this.$route.params.id, value: this.Vote, body: this.body }, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then(response => {
                    if(response.data == 'Success'){
                        this.getData()
                    } else {
                        alert('SomeThings Went Wrong')
                    }
                })
                .catch(err => {
                    console.log(err)
                })
            }
        },
        SetVote: function(e){
            this.Vote = e.target.value;
        },
        getData: function(){
            axios.get(`/api/getCourse/${this.$route.params.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then(response => {
                console.log(response)
                this.is_authenticated = response.data.authenticated
                this.Data = response.data.data;
                this.Profile = response.data.profile;
                this.NameOwner = response.data.data.owner.name
                this.OwnerID = response.data.data.owner.id
            })
            .catch(err => {
            console.log(err)
            })
        }
    }
}
</script>