<template>
  <div class="row" style="height:100px">
      <div class="col">
        <input class="form-control" type="text" v-model="query.search" placeholder="Keyword">
        <span class="badge badge-info mx-2">Gender: Male X</span>
        <span class="badge badge-info">Location: Europe X</span>
      </div>
  </div>
</template>

<script>
export default {
  name: 'searchBar',
  data () {
      return {
          sidebarOpen: true,
          searchQuery: {
            age: [25, 75]
          },
      }
  },
  params: {
    searchQuery: Object,
    sidebarOpen: Boolean,
  },
}
</script>

