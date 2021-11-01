<template>
  <div>
    <div class="auth">
        <div class="card">
          <div class="auth__header text-center">
            <a href="/">
              <img :src=" URLFile + '/public/img/icon.svg'" alt="icon" />
            </a>
            <h3>Account SignUp</h3>
            <p>Create a new developer account</p>
          </div>
          <form v-on:submit.prevent="register" class="form auth__form">

            <!-- Input:Name -->
            <div class="form__field">
              <label for="formInput#text">Name: </label>
              <input
                class="input input--text"
                id="formInput#text"
                type="text"
                placeholder="Enter your name..."
                v-model="first_name"
              />
            </div>

            <div v-if="PesanErrorName.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorName }}</div>
            </div>

            <!-- Input:Email -->
            <div class="form__field">
              <label for="formInput#text">Email: </label>
              <input
                class="input input--text"
                id="formInput#text"
                type="text"
                placeholder="Enter your email..."
                v-model="email"
              />
            </div>

            <div v-if="PesanErrorEmail.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorEmail }}</div>
            </div>

            <!-- Input:Username -->
            <div class="form__field">
              <label for="formInput#text">Username: </label>
              <input
                class="input input--text"
                id="formInput#text"
                type="text"
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
                placeholder="••••••••"
                v-model="password1"
              />
            </div>

            <div v-if="PesanErrorPassword.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorPassword }}</div>
            </div>

            <!-- Input:Confirm Password -->
            <div class="form__field">
              <label for="formInput#password">Confirm Password: </label>
              <input
                class="input input--password"
                id="formInput#passowrd"
                type="password"
                placeholder="••••••••"
                v-model="password2"
              />
            </div>

            <div v-if="PesanErrorConfirmPassword.length > 0" style="background: #dc3545; display: flex; justify-content: center; padding: 10px 0; position:relative">
              <div style="color: #fff;">{{ PesanErrorConfirmPassword }}</div>
            </div>

            <div class="auth__actions">
              <input class="btn btn--sub btn--lg" type="submit" value="Sign Up" />
            </div>
          </form>
          <div class="auth__alternative">
            <p>Already have an Account?</p>
            <router-link :to="{ name: 'login' }">Log In</router-link>
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
                first_name: "",
                email: "",
                username: "",
                password1: "",
                password2: "",
                Title: "Register | Rudemy",
                URLFile: URL,
                PesanErrorName: "",
                PesanErrorEmail: "",
                PesanErrorUsername: "",
                PesanErrorPassword: "",
                PesanErrorConfirmPassword: "",
            }
        },
        methods: {
            register: function() {
                this.incorrectAuth = false;
                this.PesanErrorName = "";
                this.PesanErrorEmail = "";
                this.PesanErrorUsername = "";
                this.PesanErrorPassword = "";
                this.PesanErrorConfirmPassword = "";

                for(let i = 1; i <= 8; i++){
                  if(this.username.length == 0 && i == 1){
                    this.incorrectAuth = true
                    this.PesanErrorUsername = "Username field cannot be empty";
                  } else if(this.password1 != this.password2 && i == 2){
                    this.incorrectAuth = true
                    this.PesanErrorPassword = "Passwords are not the same";
                  } else if(this.password1.length == 0 && i == 3){
                    this.incorrectAuth = true
                    this.PesanErrorPassword = "Password field cannot be empty";
                  } else if(this.password2.length == 0 && i == 4){
                    this.incorrectAuth = true
                    this.PesanErrorConfirmPassword = "Confirm password cannot be empty";
                  } else if(this.email.length == 0 && i == 5){
                    this.incorrectAuth = true
                    this.PesanErrorEmail = "Email field cannot be empty";
                  } else if(!this.email.includes("@") && this.email.length > 0 && i == 6){
                    this.incorrectAuth = true
                    this.PesanErrorEmail = "Email must have an @ symbol";
                  } else if(this.first_name.length == 0 && i == 7){
                    this.incorrectAuth = true
                    this.PesanErrorName = "Name field cannot be empty";
                  } else if(!this.incorrectAuth && i == 8) {
                    this.$store.dispatch('userRegis', {
                        first_name: this.first_name,
                        email: this.email,
                        username: this.username,
                        password1: this.password1,
                        password2: this.password2
                    }).then(() => {
                        this.$router.push({ name: 'login' })
                    })
                    .catch(err => {
                        console.log(err)
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
        },
    }
</script>