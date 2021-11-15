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
          <tr>
            <th>33</th>
            <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C.">Recording My First On-Campus Recruitment</a>
            </td>
            <td>User_ABC</td>
            <td>User_DEF</td>
            <td>2021-11-22 22:22:22</td>
          </tr>
          <tr>
            <th>33</th>
            <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C.">Recording My First On-Campus Recruitment</a>
            </td>
            <td>User_ABC</td>
            <td>User_DEF</td>
            <td>2021-11-22 22:22:22</td>
          </tr>
          <tr>
            <th>33</th>
            <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C.">Recording My First On-Campus Recruitment</a>
            </td>
            <td>User_ABC</td>
            <td>User_DEF</td>
            <td>2021-11-22 22:22:22</td>
          </tr>
          <tr>
            <th>33</th>
            <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C.">Recording My First On-Campus Recruitment</a>
            </td>
            <td>User_ABC</td>
            <td>User_DEF</td>
            <td>2021-11-22 22:22:22</td>
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
      <div>
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Title</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input class="input is-normal" type="text" placeholder="">
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
                <textarea class="textarea is-large" placeholder=""></textarea>
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

      </div>
    </section>

  </div>

</template>

<script>
export default {
  name: "Discussion"
}
</script>

<style scoped>

</style>