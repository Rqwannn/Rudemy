<template>
    <div>

        <main class="formPage my-xl">
            <div class="content-box">
                <div class="formWrapper">
                    <router-link class="backButton" :to="{name:'UserProfile', params: {id}}">
                         <span style="font-size: 20px;">&#8592;</span>
                    </router-link>
                    <br>

                    <form @submit.prevent="SubmitMessage()">

                        <div class="form__field">
                            <label>Name: </label>
                            <input type="text" v-model="Name" class="input">
                        </div>

                        <div class="form__field">
                            <label>Email: </label>
                            <input type="email" v-model="Email" class="input">
                        </div>

                        <div class="form__field">
                            <label>Subject: </label>
                            <input type="text" v-model="Subject" class="input">
                        </div>

                        <div class="form__field">
                            <label>Body: </label>
                            <textarea v-model="Body" class="input" style="resize: none;">Type...</textarea>
                        </div>

                        <input class="btn btn--sub btn--lg  my-md" type="submit" value="Submit" />
                    </form>
                </div>
            </div>
        </main>
    </div>
</template>
<script>
import { axios } from '../../axios-api'

export default {
    props: ['id'],
    data(){
        return {
            Name: '',
            Email: '',
            Subject: '',
            Body: '',
            Title: "Message Form | Rudemy"
        }
    },
    methods:{
        SubmitMessage: function(){
            if(this.Name == '' || this.Email == '' || this.Subject == '' || this.Body == ''){
                this.$swal(
                    'Oppsss...',
                    `Please fill in the fields first`,
                    'warning'
                )
            } else {
                const setData = {
                    'id': this.id,
                    'name': this.Name,
                    'email': this.Email,
                    'subject': this.Subject,
                    'body': this.Body
                }

                axios.post('/api/InsertMessage/', setData, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then( response => {
                    this.$swal({
                        title: 'Success',
                        text: `${response.data.Pesan}`,
                        icon: 'success',
                        showCancelButton: false,
                        confirmButtonColor: '#3085d6',
                        confirmButtonText: 'Oke'
                        }).then((result) => {
                        if (result.isConfirmed) {
                            this.$router.push({ name: 'UserProfile', params: {id: response.data.IdentityUser} })
                        }
                    })
                })
                .catch( err => console.log(err) )
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