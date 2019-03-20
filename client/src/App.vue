<template>
  <div id="app">
    <sidebar />
    <main class="page-wrap">
      <search-bar />
      <tweets />
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
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
