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
            <form id="searchForm" class="form" action="#" method="get">
              <div class="form__field">
                <label for="formInput#search">Search Developers</label>
                <input
                  class="input input--text"
                  id="formInput#search"
                  type="text"
                  name="search_query"
                  value=""
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
            <div class="column card">
              <div class="dev">
                <a href="#" class="card__body">
                  <div class="dev__profile">
                    <img
                      class="avatar avatar--md"
                      src="#"
                      alt="image"
                    />
                    <div class="dev__meta">
                      <h3>Ridwan</h3>
                      <h5>Hallo Semua</h5>
                    </div>
                  </div>
                  <p class="dev__info">
                    <!-- {{result.bio|slice:"150"}} -->
                    <!-- slice berfungsi agar karakter tidak lebih dari 150 pada saat di render -->
                  </p>
                  <div class="dev__skills">
                    <!-- Slice di sini berfungsi agar data hanya di panggil maximal 5 data -->
                    <!-- {% for skill in result.skill_set.all|slice:'5' %} -->
                    <span class="tag tag--pill tag--main">
                      <small>Django</small>
                    </span>
                    <!-- {% endfor %} -->
                  </div>
                </a>
              </div>
            </div>
            <!-- {% endfor %} -->
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
  import { axios } from '../../axios-api'
  import { mapState } from 'vuex'

  export default {
    name: 'Posts',
    data(){
      return {
        Title: 'Home | Rudemy'
      }
    },
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    components: {
      'Navbar': NavBar
    },
    computed: mapState(['APIData']), // Memanggil state APIData yang berada di store.js
    created () {
      axios.get('/api/profile/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => {
          this.$store.state.APIData = response.data
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
  }
</script>

