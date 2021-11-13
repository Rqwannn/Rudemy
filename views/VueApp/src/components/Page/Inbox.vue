<template>
    <div>
        <Navbar></Navbar>

          <main class="inbox my-xl">
            <div class="content-box">
                <h3 class="inbox__title">New Messages(<span>{{ Unread }}</span>)</h3>
                <ul class="messages">
                        <li class="message" :class="result.is_read ? '' : 'message--unread' " v-for="result in Data" :key="result.id">
                            <router-link :to="{name:'Message', params: {id: result.id}}">
                                <span class="message__author">{{ result.name }}</span>
                                <span class="message__subject">{{ result.subject }}</span>
                                <span class="message__date">{{ result.created.split('T')[0] }}</span>
                            </router-link>
                        </li>
                </ul>
            </div>
        </main>
    </div>
</template>

<script>
import { axios } from '../../axios-api'

export default {
    data(){
        return {
            Data: [],
            Unread: 0,
            Title: "Inbox | Rudemy"
        }
    },
    created(){
        axios.get(`/api/getMessage/${this.$store.state.UserData.id}`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } }).then(response => {
            this.Data = response.data.data;
            this.Unread = response.data.unred;
        }).catch(err => console.log(err));
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