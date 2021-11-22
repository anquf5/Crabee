<template>
  <div class="page-company">
    <section class="section">
      <div class="columns">
        <div class="column is-8">
          <div id="banner">
            <section class="hero">
              <div class="hero-body has-background-light">
                <article class="media">
                  <div class="media-left">
                    <figure class="image is-128x128">
                      <img v-bind:src="company.get_image" alt="Image">
                    </figure>
                  </div>
                  <div class="media-content">
                    <div class="content ml-4">
                      <span class="icon-text">
                        <span class="mr-2"><h2><strong>{{ company.name }}</strong></h2></span>
                        <span class="icon has-text-info-dark">
                          <a @click="jump(company.link)" style="cursor:pointer;">

                          </a>
                          <i class="fas fa-external-link-alt is-medium fa-lg" @click="jump(company.link)"></i>
                        </span>
                      </span>
                      <div class="ml-1">
                        <star :size="36" :score="company.get_avg"/>
                      </div>
                      <p class="mt-4 ml-1">{{ company.intro }} </p>
                    </div>
                  </div>
                </article>
              </div>
            </section>
          </div>
          <div id="review-title" class="mt-6">
            <div class="content">
              <h3><strong>Reviews <small>({{ company.get_review_num }})</small></strong></h3>
            </div>
            <button class="button is-success modal-button" data-target="review-form" @click="showForm">
                  <span class="icon-text">
                    <span class="icon">
                      <i class="fas fa-plus"></i>
                    </span>
                    <span><strong>Write a review</strong></span>
                  </span>
            </button>
            <div class="modal" v-bind:class="{'is-active': isActive}">
              <div class="modal-background"></div>
              <div class="modal-card">
                <header class="modal-card-head">
                  <p class="modal-card-title">Add Review</p>
                  <button class="delete" aria-label="close" @click="closeForm"></button>
                </header>
                <section class="modal-card-body">
                  <form @submit.prevent="addReview">

                    <div class="field">
                      <label class="label">Rate</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="formData.rate">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Interview difficulty</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="formData.difficulty">
                            <option>Easy</option>
                            <option>Normal</option>
                            <option>Difficult</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Job</label>
                      <div class="control">
                        <input class="input" placeholder="Job Title" v-model="formData.job_title">
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Review title</label>
                      <div class="control is-medium">
                        <input class="input" placeholder="Title" v-model="formData.title">
                      </div>
                    </div>

                    <div class="field">
                      <label class="label">Content</label>
                      <div class="control">
                        <textarea class="textarea" type="text" placeholder="Write your review..." v-model="formData.content"></textarea>
                      </div>
                    </div>

                    <div class="field">
                      <p class="control">
                        <button class="button is-success"><strong>Post review</strong></button>
                      </p>
                    </div>
                  </form>
                </section>
              </div>
            </div>
          </div>
          <div id="reviews" class="mt-6">
            <div v-for="review in company.review" v-bind:key="review.id" v-bind:company="company">
              <div class="columns">
                <div class="column is-2 mt-3">
                  <div class="image is-64x64">
                    <div v-if="review.get_user_avatar !== '' ">
                      <img v-bind:src="review.get_user_avatar">
                    </div>
                    <div v-else>
                      <img :src="require('../assets/default.jpg')">
                    </div>
                  </div>
                  <p>{{ review.get_reviewer }}</p>
                </div>
                <div class="column is-7">

                  <div>
                    <p class="is-size-5 has-text-grey-darker">
                      <strong>{{ review.review_title }}</strong>
                    </p>
                    <p class="is-size-6 has-text-grey ml-4 mt-4">{{ review.job_title }}</p>
                  </div>
                  <div class="block">
                    <div class="columns is-multiline">
                      <div class="column is-6">
                        <p class="is-size-6 has-text-grey ml-4">Rate: <star :size="36" :score="review.rate"/></p>
                      </div>
                      <div class="column is-6">
                        <p class="is-size-6 has-text-grey">Difficulty: <star :size="36" :score="review.iv_difficulty"/></p>
                      </div>
                      <div class="column is-12">
                        <p class="is-size-6 has-text-grey-darker">{{ review.review_cont }}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="column is-3">
                  <p class="is-size-6 has-text-grey">{{ review.get_pubtime }}</p>
                </div>
              </div>
              <hr>
            </div>
          </div>

        </div>
        <div class="column is-4">
          <OtherCompanies></OtherCompanies>
        </div>
      </div>
    </section>
  </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import CompanyBox from "../components/CompanyBox.vue";
import OtherCompanies from "../components/OtherCompanies";
import star from "../components/star";
export default {
  name: "Company",
  data(){

    return{
      company:{},
      formData: {
        id: this.$route.params.id,
        rate: '',
        difficulty: '',
        job_title: '',
        title: '',
        content:'',
      },
      otherCompanies:[],
      isActive : false
    }
  },
  components: {
    OtherCompanies,
    CompanyBox,
    star
  },
  mounted() {
    this.getCompany()
    this.getOtherCompanies()
  },
  methods: {
    getCompany(){
      const id=this.$route.params.id

      axios
        .get(`/api/company/${id}/`)
        .then(response => {
          this.company = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getOtherCompanies(){
      axios
          .get('/api/company/')
          .then(response => {
            this.otherCompanies = response.data
                // .filter(company => company.id !== this.cid)
          })
          .catch(error => {
            console.log(error)
          })
    },
    addReview(){
      axios.post('/api/company_review/add/', {
        'cid': this.formData.id,
        'job': this.formData.job_title,
        'title': this.formData.title,
        'content': this.formData.content,
        'rate': this.formData.rate,
        'difficulty': this.formData.difficulty,
      })
      .then(response => {
        this.closeForm();
        location.reload();
      })

      toast({
        message: 'This review was added!',
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })
    },
    showForm(){
      this.isActive = true
    },
    closeForm(){
      this.isActive = false
    },
    jump(link){
      window.location.href=link;
    }
  }
}
</script>

<style scoped>

</style>
