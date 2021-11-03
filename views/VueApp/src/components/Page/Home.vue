<template>
  <div>
    <Navbar></Navbar> 

    <main class="home">
      <section class="hero-section text-center">
        <div class="container container--narrow">
          <div class="hero-section__box">
            <h2>CONNECT WITH <span>DEVELOPERS</span></h2>
            <h2>FROM AROUND THE WORLD</h2>
          </div>

          <div class="hero-section__search">
            <form id="searchForm" class="form" @submit.prevent="SearchDev">
              <div class="form__field">
                <label for="formInput#search">Search Developers</label>
                <input
                  class="input input--text"
                  id="formInput#search"
                  type="text"
                  name="search_query"
                  v-model="SearchData"
                  placeholder="Search by developer name or short intro"
                />
              </div>

              <input class="btn btn--sub btn--lg" type="submit" value="Search" />
            </form>
          </div>
        </div>
      </section>
      <!-- Search Result: DevList -->
      <section class="devlist">
        <div class="container">
          <div class="grid grid--three">

            <div class="column card" v-for="result in APIData" :key="result.id">
              <div class="dev">
                <a href="#" class="card__body">
                  <div class="dev__profile">
                    <img
                      class="avatar avatar--md"
                      :src="Path + '' + result.profile_image"
                      alt="image"
                    />
                    <div class="dev__meta">
                      <h3>{{ result.name }}</h3>
                      <h5>{{ result.short_intro }}</h5>
                    </div>
                  </div>
                  <p class="dev__info">
                    {{ result.bio }}
                  </p>
                  <div class="dev__skills">

                    <span class="tag tag--pill tag--main" v-for="skill in result.skill" :key="skill.id">
                      <small>{{ skill.name }}</small>
                    </span>

                  </div>
                </a>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- with dan seterusnya menandakan jika query akan mendapat data dari instance project yang di berikan di view -->
      
      <!-- {% include 'pagination.html' with query=data custom_range=custom_range %} -->

    </main>
  </div>
</template>

<script>
  import NavBar from '../Template/Navbar'
  import Pagination from '../Template/Pagination'
  import { URL } from '../../ApiBaseUrl'
  import { axios } from '../../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Posts',
    data(){
      return {
        Title: 'Home | Rudemy',
        Path: URL,
        SearchData: ""
      }
    },
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    components: {
      'Navbar': NavBar,
      'Pagination': Pagination
    },
    computed: mapState(['APIData']), // Memanggil state APIData yang berada di store.js
    created () {
      axios.get('/api/profile/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => {
          this.$store.state.APIData = response.data.data;
        })
        .catch(err => {
          console.log(err)
        })
    },
    watch: {
      title: {
        immediate: true,
          handler() {
            document.title = this.Title;
          }
        },
      },
      methods:{
        SearchDev: function(){
          const Data = {
            'search_query': this.SearchData
          }

          axios.post('/api/profile/', Data, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.$store.state.APIData = response.data.data;
          })
          .catch(err => {
            console.log(err)
          })
        }
      }
  }
</script>

