<template>
    <div>
        <Navbar></Navbar>

          <main class="projects">
            <section class="hero-section text-center">
                <div class="container container--narrow">
                    <div class="hero-section__box">
                        <h2>Search for <span>Course</span></h2>
                    </div>
  
                    <div class="hero-section__search">
                    <form id="searchForm" class="form" @submit.prevent="SearchDev">
                        <div class="form__field">
                        <label for="formInput#search">Search By Course</label>
                        <input class="input input--text" id="formInput#search" type="text" v-model="SearchData"
                            placeholder="Search by Project Title" />
                        </div>

                        <input class="btn btn--sub btn--lg" type="submit" value="Search" />
                    </form>
                    </div>
                </div>
            </section>

            <section class="projectsList">
                <div class="container">
                    <div class="grid grid--three">

                        <div class="column" v-for="result in APIData.results" :key="result.id">
                            <div class="card project">
                                <router-link :to="{name:'UserCourse', params: {id: result.id}}" class="project">
                                  <img class="project__thumbnail" :src="result.featured_image" alt="project thumbnail" />
                                  <div class="card__body">
                                      <h3 class="project__title">{{ result.title }}</h3>
                                      <p><a class="project__author" href="#">{{ result.description }}</a></p>
                                      <p class="project--rating">
                                          <span style="font-weight: bold;">{{ result.vote_ratio }}%</span> Positive
                                          Feedback ({{result.vote_total}} Vote{{result.vote_total > 1 ? 's' : ''}} )
                                      </p>
                                      <div class="project__tags">
                                          <span class="tag tag--pill tag--main" v-for="item in result.tags" :key="item.id">
                                              <small>{{ item.name }}</small>
                                          </span>
                                      </div>
                                  </div>
                                </router-link>
                            </div>
                        </div>

                    </div>
                </div>
            </section>

            <Pagination></Pagination>

        </main>
    </div>
</template>

<script>
  import NavBar from '../Template/Navbar'
  import Pagination from '../Template/Pagination'
  import { axios } from '../../axios-api'
  import { mapState } from 'vuex'

export default {
    data(){
        return {
            Title: 'Course | Rudemy',
            SearchData: "",
        }
    },
    components: {
        'Navbar': NavBar,
        'Pagination': Pagination
    },
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    computed: mapState(['APIData']),
    created(){
        this.$store.state.StatusPaginate = 'course';

        axios.get('/api/course/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => {
          this.$store.state.APIData = response.data;
          
          if(response.data.next != null){
            const PisahPath = response.data.next.split("/");
            const AmbilTerakhir = PisahPath[PisahPath.length - 1];
            this.$store.state.PaginationNext = AmbilTerakhir;
          }

          if(response.data.previous != null){
            const PisahPath = response.data.previous.split("/");
            const AmbilTerakhir = PisahPath[PisahPath.length - 1];
            this.$store.state.PaginationPrev = AmbilTerakhir;
          } 
          
          if(response.data.count > response.data.results.length){
            this.$router.push(`${this.$route.path}?page=1`).catch(() => {});
          }

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
            this.$store.commit('setPath', { path: this.$route.fullPath })
          }
        },
      },
    methods: {
        SearchDev: function(){
          let SetupPath = '';
          const ReplacePath = this.$route.fullPath.split('?');

          ReplacePath.forEach( ( data, number ) => {
            if(number > 0){
              if(number < 2){
                SetupPath += `?${data}`
              } else {
                SetupPath += `${data}`
              }
            } else {
              SetupPath += `${data}/`
            }
          })

          let URLPattern = `/api${SetupPath.toLowerCase()}` 
          this.$store.state.SearchQuery = this.SearchData;

          if(this.SearchData != ""){
            URLPattern += `&search_query=${this.SearchData}`
          } else {
            URLPattern = `/api/course/`;
            this.$router.push('/Course?page=1').catch(() => {});
          }
          axios.get(URLPattern, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.$store.state.APIData = response.data;
          })
          .catch(err => {
            console.log(err)
          })
        }
    }
}
</script>