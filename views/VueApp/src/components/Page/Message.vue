<template>
    <div>
        <Navbar></Navbar>

          <main class="messagePage my-xl">
            <div class="content-box">
                <div class="message">
                    <router-link class="backButton" :to="{name:'Inbox'}">
                         <span style="font-size: 20px;">&#8592;</span>
                    </router-link>
                    <h2 class="message__subject">{{ Data.subject }}</h2>
                    <router-link v-if="Data.sender" class="message__author" :to="{name:'UserProfile', params: {id: Data.id}}">
                        <i class="im im-angle-left"></i>
                    </router-link>
                    <p v-else class="message__author">{{Data.name}}</p>
                    <p class="message__date">{{Data.created.split('T')[0]}}</p>
                    <div class="message__body">
                        {{Data.body}}
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import NavBar from '../Template/Navbar'
import { axios } from '../../axios-api'

export default {
    data(){
        return {
            Data: [],
        }
    },
    props: ['id'],
    components: {
        'Navbar': NavBar
    },
    created(){
        this.getData()
    },
    methods:{
        getData: function(){
            axios.get(`/api/UserMassage/${this.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then( response => {
                    this.Data = response.data;
                    console.log(this.Data)
                }).catch( err => console.log(err) )
        }
    }
}
</script>