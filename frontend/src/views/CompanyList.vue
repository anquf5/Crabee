<template>
  <div class="home">
    <section class="section">
      <form method="get" action="/search">
        <div class="field is-grouped mb-6">
          <div class="control is-expanded">
            <input class="input" type="text" placeholder="Input Company Name .." name="query">
          </div>
          <div class="control">
            <button class="button is-success">
                <span class="icon-text">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                  <span>Search</span>
                </span>
            </button>
          </div>
        </div>
      </form>
      <div class="columns is-multiline">
        <div class="column is-12">
          <p class="is-size-4 has-text-start mb-2"><strong>Explore Companies</strong></p>
        </div>
        <CompanyBox v-for="company in companies" v-bind:key="company.id" v-bind:company="company">
        </CompanyBox>
      </div>
    </section>
  </div>
</template>

<script>
import CompanyBox from "../components/CompanyBox";
import axios from "axios";

export default {
  name: "CompanyList",
  data() {
    return {
      companies: []
    }
  },
  components: {
    CompanyBox
  },
  mounted() {
    this.getCompanies()
  },
  methods: {
    getCompanies(){
      axios
          .get('/api/company/')
          .then(response => {
            this.companies = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>

</style>
