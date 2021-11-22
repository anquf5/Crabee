<template>
  <div class="block">
    <section class="section">
      <div>
        <table class="table is-fullwidth is-striped is-hoverable">
          <thead>
          <tr>
            <th>Reply</th>
            <th>Title</th>
            <th>Creator</th>
            <th>Last Reply</th>
            <th>Update Time</th>
          </tr>
          </thead>
          <tfoot>
          <tr>
            <th>Reply</th>
            <th>Title</th>
            <th>Creator</th>
            <th>Last Reply</th>
            <th>Update Time</th>
          </tr>
          </tfoot>
          <tbody>
          <tr v-for="topic in topics" v-bind:key="topic.id">
            <th>{{ topic.get_reply_num }}</th>
            <td><router-link v-bind:to= "topic.get_absolute_url">{{ topic.title }}</router-link>
            </td>
            <td>{{ topic.get_creator }}</td>
            <td>{{ topic.get_last_replier }}</td>
            <td>{{ topic.get_update_time }}</td>
          </tr>
          </tbody>
        </table>
      </div>
      <div id="page" class="block">
        <nav class="pagination is-small" role="navigation" aria-label="pagination">
          <a class="pagination-previous">Previous</a>
          <a class="pagination-next">Next page</a>
          <ul class="pagination-list">
            <li><a class="pagination-link" aria-label="Goto page 1">1</a></li>
            <li><span class="pagination-ellipsis">&hellip;</span></li>
            <li><a class="pagination-link" aria-label="Goto page 45">45</a></li>
            <li><a class="pagination-link is-current" aria-label="Page 46" aria-current="page">46</a></li>
            <li><a class="pagination-link" aria-label="Goto page 47">47</a></li>
            <li><span class="pagination-ellipsis">&hellip;</span></li>
            <li><a class="pagination-link" aria-label="Goto page 86">86</a></li>
          </ul>
        </nav>
      </div>
      <form @submit.prevent="addTopic">
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Title</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input class="input is-normal" type="text" placeholder="" v-model="formData.title">
              </div>
            </div>
          </div>
        </div>


        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Description</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <textarea class="textarea" type="text" placeholder="" v-model="formData.content"></textarea>
              </div>
            </div>
          </div>
        </div>

        <div class="field is-horizontal">
          <div class="field-label">
            <!-- Left empty for spacing -->
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <button class="button is-primary">
                  Submit
                </button>
              </div>
            </div>
          </div>
        </div>

      </form>
    </section>

  </div>

</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  inject:['reload'],
  name: "Discussion",
  data() {
    return {
      topics: [],
      formData: {
        title: '',
        content: '',
      }
    }
  },
  components: {

  },
  mounted() {
    this.getTopics()
  },
  methods: {
    getTopics(){
      axios
          .get('/api/topic/')
          .then(response => {
            this.topics = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    addTopic(){
      axios.post('/api/topic/add/', {
        'title': this.formData.title,
        'content': this.formData.content
      })
      .then((response => {
        toast({
          message: 'This topic was added!',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
      }))
      .then(response => {
        location.reload();
      })

    }
  }
}
</script>

<style scoped>

</style>
