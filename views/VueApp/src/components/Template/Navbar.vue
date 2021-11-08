<template>
  <div>
    <header class="header">
      <div class="container container--narrow">
        <a :href="{name:'Home'}" class="header__logo" style="color: #fff;">
         Rudemy
        </a>
        <nav class="header__nav">
          <input type="checkbox" id="responsive-menu" />
          <label for="responsive-menu" class="toggle-menu">
            <span>Menu</span>
            <div class="toggle-menu__lines"></div>
          </label>
          <ul class="header__menu">
            <router-link tag="li" class="header__menuItem" :to="{name:'Home'}">
              <a href="#" style="color: #fff;">
                Developers
              </a>
            </router-link>
            <router-link tag="li" class="header__menuItem" :to="{name:'Course'}">
              <a href="#" style="color: #fff;">
                Course
              </a>
            </router-link>
            <router-link tag="li" class="header__menuItem" :to="{name:'Inbox'}">
              <a href="#" style="color: #fff;">
                Inbox
              </a>
            </router-link>
            <router-link tag="li" class="header__menuItem" :to="{name:'Account'}">
              <a href="#" style="color: #fff;">
                Account
              </a>
            </router-link>
            <router-link v-if="Permissions" class="btn btn--sub" style="color: #fff;" tag="li" :to="{name:'logout'}">Logout</router-link>
            <router-link v-else class="btn btn--sub" style="color: #fff;" tag="li" :to="{name:'login'}">Login/Sign Up</router-link>
          </ul>
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  
  export default {
    name: 'Navbar',
    computed: mapState(['accessToken', 'Permissions'])
  }
</script>

<style scoped>
    a {
      color:#000;
  }
</style>