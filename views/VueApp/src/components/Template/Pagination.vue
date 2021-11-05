<template>
    <div>
        <div class="pagination" v-if="Next != '' || Prev != ''">
            <ul class="container">
                <li v-if="Prev != ''">
                    <a :href="Prev" class="btn page-link" @click.prevent="ClickPagination($event)" :data-page="Prev">Prev</a>
                </li>

                <li v-for="result in Data.count - Data.results.length" :key="result">
                    <a :href="'?page=' + result " v-if="result == AktifPage" id="PagePagination" @click.prevent="ClickPagination($event)" :data-page="'?page=' + result" class="btn page-link CheckIndex btn--sub">{{ result }}</a>
                    <a :href="'?page=' + result " v-else @click.prevent="ClickPagination($event)" :data-page="'?page=' + result " class="btn CheckIndex page-link">{{ result }}</a>
                </li>

                <li v-if="Next != ''">
                    <a :href="Next" class="btn page-link" @click.prevent="ClickPagination($event)" :data-page="Next">Next</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import { axios } from '../../axios-api'

export default {
    data(){
        return {
            Data: [],
            Next: '',
            Prev: '',
            LeftIndex: 0,
            RightIndex: 0,
            AktifPage: 1,
        }
    },
    created(){
        this.Data = this.$store.state.APIData;
        this.Next = this.$store.state.PaginationNext;
        this.Prev = this.$store.state.PaginationPrev;
    },
    updated(){
        this.AktifPage = this.$route.query.page;
        this.CostumTotalBTN()
    },
    computed: {
        change () {
            return this.$store.state.APIData
        }
    },
    watch: {
        change (newData, oldData) {
            this.checkNextPrev(newData);
        }
    },
    methods: {
        CostumTotalBTN: function(){
            const Page = this.$route.query.page;
            let leftIndex = parseInt(Page) - 1;

            if (leftIndex < 1){
                leftIndex = 1
            }

            let rightIndex = parseInt(Page) + 1;

            if( rightIndex > Page){
                rightIndex = parseInt(Page)
            }

            this.LeftIndex = leftIndex;
            this.RightIndex = rightIndex;
        },
        checkNextPrev: function(data){
              if(data.next != null){
                    const PisahPath = data.next.split("/");
                    const AmbilTerakhir = PisahPath[PisahPath.length - 1];
                    const urlParams = new URLSearchParams(AmbilTerakhir);
                    this.Next = `?page=${urlParams.get('page')}`;
                } else {
                    this.Next = '';
                }

                if(data.previous != null){
                    const PisahPath = data.previous.split("/");
                    const AmbilTerakhir = PisahPath[PisahPath.length - 1];

                    if(AmbilTerakhir == '' || (AmbilTerakhir.includes('search_query') && !AmbilTerakhir.includes('page') )){
                        this.Prev = '?page=1';
                    } else {
                        const urlParams = new URLSearchParams(AmbilTerakhir);
                        this.Prev = `?page=${urlParams.get('page')}`;
                    }

                } else {
                    this.Prev = '';
                }
        },
        ClickPagination: function(e){
          let setParams = e.target.dataset.page

          if(setParams == ""){
              setParams = '?page=1'
          }
          
          let URL = `/api/${this.$store.state.StatusPaginate}/${setParams}`;

          let URLPath = `${this.$route.path}${setParams}`
          if(this.$store.state.SearchQuery != ""){
              URL += `&search_query=${this.$store.state.SearchQuery}`
              URLPath += `&search_query=${this.$store.state.SearchQuery}`
          }

          axios.get(URL, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
                this.checkNextPrev(response)
                this.$store.state.APIData = response.data;
          })
          .catch(err => {
            console.log(err)
          })

          this.$router.push(URLPath).catch(() => {});
        }
    }
}
</script>