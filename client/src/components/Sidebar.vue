<template>
    <Slide>
      <a id="home" href="#">
        <span>Home</span>
      </a>
    </Slide>
</template>

<script>
import { Slide } from 'vue-burger-menu'  // import the CSS transitions you wish to use, in this case we are using `Slide`
 
export default {
    components: {
        Slide // Register your component
    }
}
</script>

