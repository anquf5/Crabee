<template>
  <section class="section">
    <section class="hero is-small is-info">
      <div class="hero-body">
        <p class="is-size-4"><strong>
          {{ topic.title }}
        </strong>
        </p>
        <button class="button is-small mt-4">Reply</button>
      </div>
    </section>
    <div>
      <div class="tile is-ancestor mt-4 mb-4">
        <div class="tile is-parent is-3">
          <article class="tile is-child box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
              </div>
              <div class="media-content">
                <p>{{ topic.get_creator }}</p>
              </div>
            </article>
          </article>
        </div>
        <div class="tile is-parent is-9">
          <article class="tile is-child">
            <p class="mx-5">{{ topic.topic_cont }}</p>
          </article>
        </div>
      </div>
    </div>
    <div v-for="reply in topic.reply" v-bind:key="reply.id" v-bind:topic="topic">
      <div class="tile is-ancestor mt-4 mb-4">
        <div class="tile is-parent is-3">
          <article class="tile is-child box">
            <article class="media">
              <div class="media-left">
                <figure class="image is-64x64">
                  <img src="https://bulma.io/images/placeholders/128x128.png">
                </figure>
              </div>
              <div class="media-content">
                <p>{{ reply.get_replier }}</p>
              </div>
            </article>
          </article>
        </div>
        <div class="tile is-parent is-9">
          <article class="tile is-child">
            <p class="mx-5">{{ reply.reply_cont }}</p>
          </article>
        </div>
      </div>
    </div>
    <div id="reply">
      <article class="media">
        <figure class="media-left">
          <p class="image is-64x64">
            <img src="https://bulma.io/images/placeholders/128x128.png">
          </p>
        </figure>
        <div class="media-content">
          <div class="field">
            <p class="control">
              <textarea class="textarea" placeholder="Add a comment..."></textarea>
            </p>
          </div>
          <div class="field">
            <p class="control">
              <button class="button">Post comment</button>
            </p>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "TopicDetail",
  data(){
    return{
      topic:{},
    }
  },
  mounted() {
    this.getTopic()
  },
  methods: {
    getTopic(){
      const id=this.$route.params.id

      axios
          .get(`/api/topic/${id}/`)
          .then(response => {
            this.topic = response.data
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