<template>
  <section class="section">
    <div class="columns is-multiline">
      <p class="is-size-5 mb-2"><strong>Find other companies</strong></p>
      <div class="column is-full" v-for="company in companies" v-bind:key="company.id">
        <router-link target="_blank" v-bind:to= "company.get_absolute_url">
          <div class="box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img v-bind:src="company.get_image" alt="Image">
                </figure>
              </div>
              <div class="content">
                <h4>
                  <strong>{{ company.name }}</strong>
                </h4>
                <p><star :size="36" :score="company.get_avg" :max_length="5"/></p>
              </div>
            </article>
          </div>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import star from '../components/star.vue'

export default {
  name: "OtherCompanies",
  data(){
    return{
      companies:[],
    }
  },
  components: {star},
  mounted() {
    this.getOtherCompanies()
  },
  methods:{
    getOtherCompanies(){
      const id=this.$route.params.id
      axios
          .post('/api/company/',{'company_id':id})
          .then(response => {
            this.companies = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  }
}
</script>

<style scoped>

</style>
