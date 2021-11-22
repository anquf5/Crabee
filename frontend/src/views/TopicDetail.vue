<template>
  <section class="section">
    <section class="hero is-small is-info">
      <div class="hero-body">
        <p class="is-size-4"><strong>
          {{ topic.title }}
        </strong>
        </p>
        <button class="button is-small mt-4" @click="go_to_reply">Reply</button>
      </div>
    </section>
    <div>
      <div class="tile is-ancestor mt-4 mb-4">
        <div class="tile is-parent is-3">
          <article class="tile is-child">
            <article class="media">
              <div class="media-left">
                <div class="image is-64x64">
                  <div v-if="topic.get_user_avatar !== '' ">
                    <img v-bind:src="topic.get_user_avatar">
                  </div>
                  <div v-else>
                    <img :src="require('../assets/default.jpg')">
                  </div>
                </div>
              </div>
              <div class="media-content">
                <p>{{ topic.get_creator }}</p>
              </div>
            </article>
          </article>
        </div>
        <div class="tile is-parent is-6">
          <article class="tile is-child">
            <p class="mx-5">{{ topic.topic_cont }}</p>
          </article>
        </div>
        <div class="tile is-parent is-3">
          <article class="tile is-child">
            <p class="mx-5">{{ topic.get_pubtime }}</p>
          </article>
        </div>
      </div>
      <hr>
    </div>
    <div v-for="reply in topic.reply" v-bind:key="reply.id" v-bind:topic="topic">
      <div class="tile is-ancestor mt-4 mb-4">
        <div class="tile is-parent is-3">
          <article class="tile is-child">
            <article class="media">
              <div class="media-left">
                <div class="image is-64x64">
                  <div v-if="reply.get_user_avatar !== '' ">
                    <img v-bind:src="reply.get_user_avatar">
                  </div>
                  <div v-else>
                    <img :src="require('../assets/default.jpg')">
                  </div>
                </div>
              </div>
              <div class="media-content">
                <p>{{ reply.get_username }}</p>
              </div>
            </article>
          </article>
        </div>
        <div class="tile is-parent is-6">
          <article class="tile is-child">
            <p class="mx-5">{{ reply.reply_cont }}</p>
          </article>
        </div>
        <div class="tile is-parent is-3">
          <article class="tile is-child">
            <p class="mx-5">{{ reply.get_pubtime }}</p>
          </article>
        </div>
      </div>
      <hr>
    </div>

    <form id="reply" @submit.prevent="addReply">
      <article class="media">
        <figure class="media-left">
          <p class="image is-64x64">
            <img src="https://bulma.io/images/placeholders/128x128.png">
          </p>
        </figure>
        <div class="media-content">
          <div class="field">
            <p class="control">
              <textarea class="textarea" placeholder="Add a comment..." v-model="formData.content"></textarea>
            </p>
          </div>
          <div class="field">
            <p class="control">
              <button class="button">Reply</button>
            </p>
          </div>
        </div>
      </article>
    </form>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "TopicDetail",
  data(){
    return{
      topic:{},
      formData: {
        id: this.$route.params.id,
        content:'',
      }
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
    addReply(){
      const id=this.$route.params.id
      axios.post('/api/topic/reply/',{
        'tid': this.formData.id,
        'content': this.formData.content,
      })
      .then(response => {
        location.reload();
      })
    },
    go_to_reply(){
      const jump = document.querySelector("#reply");
      if(!!jump) {
        jump.scrollIntoView(true);
      }
      document.querySelector("go_to_reply").scrollIntoView(true);
    }
  }
}
</script>

<style scoped>

</style>
