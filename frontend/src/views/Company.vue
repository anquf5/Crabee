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
                  <h4 class="mt-6"><strong>Reviews</strong></h4>
                  <article class="media mt-4">
                    <div class="media-content">
                      <div class="field">
                        <p class="control">
                          <textarea class="textarea" placeholder="Write your review..."></textarea>
                        </p>
                      </div>
                      <div class="field">
                        <p class="control">
                          <button class="button">Post comment</button>
                        </p>
                      </div>
                    </div>
                  </article>
                  <div v-for="review in company.reviews" v-bind:key="review.id" v-bind:company="company">
                    <article class="media">
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
                              <strong>A Good Experience </strong>
                            </p>
                            <p>Rate: 4.5 Difficulty: Medium</p>
                            <p>Java Developer</p>
                            <p class="is-size-6 has-text-grey">The Company always kept up to their price promise, but not too sure what it means to buy now pay later as you are required to pay interest from the day you purchased the item?</p>
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
      company:{
        "id": 2,
        "name": "Amazon",
        "intro": "b company",
        "link": "www.amazon.com",
        "get_avg": 3,
        "get_review_num": 1,
        "review": [
          {
            "id": 3,
            "job_title": "JAVA Developer",
            "review_title": "a pleasure interview experience",
            "review_cont": "aaaa",
            "pub_date": "2021-11-11T16:40:54.327489Z",
            "rating": 3,
            "iv_difficulty": 1,
            "get_reviewer": "diablo"
          }
        ]
      },
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
  }
}
</script>

<style scoped>

</style>