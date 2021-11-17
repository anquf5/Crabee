<template>
  <div class="page-company">
    <section class="section">
      <div class="tile is-ancestor">
        <div class="tile is-vertical is-9">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <div class="tile is-child box has-background-light">
                <article class="media">
                  <div class="media-left">
                    <figure class="image is-128x128">
                      <img src="https://media-exp1.licdn.com/dms/image/C560BAQHTvZwCx4p2Qg/company-logo_100_100/0/1612205615891?e=1645056000&v=beta&t=GQCAhBJWrUvKi2FCuKj6CspWqTp6OW_JQoKjQFr1fvc" alt="Image">
                    </figure>
                  </div>
                  <div class="media-content">
                    <div class="content ml-4">
                      <h2>
                        <strong>{{ company.name }}</strong>
                      </h2>
                      <p>{{ company.intro }} </p>
                      <small>Rate: {{ company.get_avg }}</small>
                    </div>
                  </div>
                </article>
              </div>
              <div class="tile is-child block">
                <div class="content">
                  <h3 class="mt-6"><strong>Reviews <small>({{ company.get_review_num }})</small></strong></h3>
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
                            <textarea class="textarea" type="text" placeholder="Write your review..."></textarea>
                          </div>
                      </div>

                      <div class="field">
                        <p class="control">
                          <button class="button is-success">Post comment</button>
                        </p>
                      </div>
                    </form>



                  <div v-for="review in company.review" v-bind:key="review.id" v-bind:company="company">
                    <article class="media mt-4">
                      <figure class="media-left">
                        <p class="image is-64x64">
                          <img src="https://bulma.io/images/placeholders/128x128.png">
                        </p>
                        <p>{{ review.get_reviewer }}</p>
                      </figure>
                      <div class="media-content">
                        <div class="content">
                          <div>
                            <p class="is-size-4 has-text-grey-darker">
                              <strong>{{ review.review_title }}</strong>
                            </p>
                            <p>Rate: {{ review.rating }} Difficulty: {{ review.iv_difficulty }}</p>
                            <p>{{ review.job_title }}</p>
                            <p class="is-size-6 has-text-grey">{{ review.review_cont }}</p>
                            <br>
                          </div>
                        </div>
                      </div>
                    </article>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tile is-parent">
          <div class="tile is-child block">
            <div class="content">
              <h4><strong>Find Other Companies</strong></h4>
            </div>
            <div class="tile box">
              <article class="media">
                <div class="media-left">
                  <figure class="image is-64x64">
                    <img src="https://media-exp1.licdn.com/dms/image/C4D0BAQHiNSL4Or29cg/company-logo_100_100/0/1519856215226?e=1645056000&v=beta&t=o9fR5v6Tzxub5ubgC-SVQigTqvdw6Rqt5WlpJpRJF9U" alt="Image">
                  </figure>
                </div>
                <div class="media-content">
                  <div class="content">
                    <h4>
                      <strong>Google</strong>
                    </h4>
                    <small>Rate:</small><br/>
                    <small>Difficulty:</small>
                  </div>
                </div>
              </article>




            </div>
            <div class="tile box">

            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
  name: "Company",
  data(){
    return{
      company:{},
      formData: {
        rate: '',
        difficulty: '',
        job_title: '',
        title: '',
        content:'',
      }
    }
  },
  mounted() {
    this.getCompanies()
  },
  methods: {
    getCompanies(){
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
    addReview(){
      const id = this.$route.params.id

      axios.post("/api/company_review/add/", {
        'cid': id,
        'job': this.formData.job_title,
        'title': this.formData.title,
        'content': this.formData.content,
        'rate': this.formData.rate,
        'difficulty': this.formData.difficulty,
      })
      .then(response => {
        if(response.data.msg === 1){
          this.$router.push({path:"/"});
      }})

    },
  }
}
</script>

<style scoped>

</style>
