<template>
  <div id="app">
    <sidebar :isOpen="sidebarOpen" :query="searchQuery"/>
    <main id="page-wrap">
      <div class="container mt-4">
        <search-bar :isOpen="sidebarOpen" :query="searchQuery" />
        <tweets />
      </div>
    </main>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'
import Tweets from './components/Tweets.vue'
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'app',
  components: {
    Sidebar,
    Tweets,
    SearchBar,
  },
  data () {
      return {
          sidebarOpen: true,
          searchQuery: {
            age: [25, 75],
            search: "",
            location: "",
            gender: "",
            language: "",
          },
      }
  },
  params: {
    searchQuery: Object,
    sidebarOpen: Boolean,
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

</style>
