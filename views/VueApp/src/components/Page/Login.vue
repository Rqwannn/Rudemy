<template>
  <div>
    <div class="auth">
        <div class="card">
          <div class="auth__header text-center">
            <a href="/">
              <img :src=" URLFile + '/public/img/icon.svg'" alt="icon" />
            </a>
            <h3>Account Login</h3>
            <p>Hello Developer, Welcome Back!</p>
          </div>
          
          <form v-on:submit.prevent="login" class="form auth__form">

            <!-- Input:Username -->
            <div class="form__field">
              <label for="formInput#text">Username: </label>
              <input
                class="input input--text"
                id="formInput#text"
                type="text"
                name="username"
                placeholder="Enter your username..."
                v-model="username"
              />
            </div>

            <div v-if="PesanErrorUsername.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorUsername }}</div>
            </div>
  
            <!-- Input:Password -->
            <div class="form__field">
              <label for="formInput#password">Password: </label>
              <input
                class="input input--password"
                id="formInput#passowrd"
                type="password"
                name="password"
                placeholder="••••••••"
                v-model="password"
              />
            </div>

            <div v-if="PesanErrorPassword.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorPassword }}</div>
            </div>

            <div class="auth__actions">
              <input class="btn btn--sub btn--lg" type="submit" value="Log In" />
            </div>
          </form>
          <div class="auth__alternative">
            <p>Don’t have an Account?</p>
            <router-link :to="{ name: 'Register' }">Sign Up</router-link>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
    import { URL } from "../../ApiBaseUrl"

    export default {
        data() {
            return {
                incorrectAuth: false,
                username: "",
                password: "",
                Title: "Login | Rudemy",
                URLFile: URL,
                PesanErrorUsername: "",
                PesanErrorPassword: "",
            }
        },
        methods: {
            login: function() {
                this.incorrectAuth = false;
                this.PesanErrorUsername = "";
                this.PesanErrorPassword = "";

                for(let i = 1; i <= 3; i++){
                  if(this.username.length == 0 && i == 1){
                    this.incorrectAuth = true
                    this.PesanErrorUsername = "Username field cannot be empty";
                  } else if(this.password.length == 0 && i == 2){
                    this.incorrectAuth = true
                    this.PesanErrorPassword = "Password field cannot be empty";
                  } else if(!this.incorrectAuth && i == 3) {
                    this.$store.dispatch('userLogin', {
                        username: this.username,
                        password: this.password
                    }).then(() => {
                        this.$router.push({ name: 'Home' })
                    })
                    .catch(err => {
                        if (err.response.status === 401) {
                          this.$swal(
                              'Oppsss...',
                              `${this.$store.state.message}`,
                              'error'
                          )
                        }
                    })
                  }
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
        }
    }
</script>
