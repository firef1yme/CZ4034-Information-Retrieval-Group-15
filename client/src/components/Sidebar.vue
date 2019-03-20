<template>
    <PushRotate disableOutsideClick noOverlay>
        <div class="flex brand">
            <img height="100px" src="../assets/logo-white.png" alt="">
            <span class="align-self-center">
                Nanyang
                Analytica
            </span>
        </div>
                
        <div class="row">
            <div class="col-12">
                <form>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Language</label>
                        <select class="form-control">
                            <option>English</option>
                            <option>Spanish</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Location</label>
                        <select class="form-control">
                            <option>Europe</option>
                            <option>Asia</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Gender</label>
                        <select class="form-control">
                            <option>Male</option>
                            <option>Female</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="customRange1">Age</label>
                        <vue-slider v-model="age" />
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Dynamically load Twitter data</label>
                        <small class="form-text text-muted mt-0 mb-1">Can take up to few minutes.</small>
  
                    </div>
                    <button type="submit" class="btn btn-info">Submit</button>
                </form>
            </div>
        </div>
        

    </PushRotate>
</template> 

<script>
import { PushRotate } from 'vue-burger-menu';
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'

export default {
    components: {
        PushRotate,
        VueSlider,
    },
    data () {
        return {
            age: [25, 75],
        }
  }
}
</script>

<style>
.brand {
    font-size: 20px;
    font-weight: 900;
}

.bm-item-list {
    font-size: 15px;
}
</style>

