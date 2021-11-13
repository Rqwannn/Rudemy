<template>
    <div>
        <main class="formPage my-xl">
            <div class="content-box">
                <div class="formWrapper">
                    <router-link class="backButton" :to="{name:'Account'}">
                         <span style="font-size: 20px;">&#8592;</span>
                    </router-link>
                    <br>

                    <form @submit.prevent="SubmitSKill()">

                        <div class="form__field">
                            <label for="formInput#text">Your Skill: </label>
                            <input type="text" v-model="Skill" placeholder="Type Your Skill" class="input">
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
    data(){
        return {
            Title: 'Insert Skills | Rudemy',
            Skill: ''
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
        SubmitSKill: function() {
            this.$swal({
                title: 'Attention',
                text: `Make sure what you have typed is correct`,
                icon: 'warning',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'Ok'
                }).then((result) => {
                if (result.isConfirmed) {
                    axios.post('/api/InsertSkill/', { newskills: this.Skill } ,{ headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                    .then( response => {
                        if(response.data.status){
                            this.$swal({
                                title: 'Success',
                                text: `${response.data.message}`,
                                icon: 'success',
                                showCancelButton: false,
                                confirmButtonColor: '#3085d6',
                                confirmButtonText: 'Ok'
                            }).then((item) => {
                                if(item.isConfirmed){
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
            })
        }
    }
}

</script>