import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    details: "",
    allProducts: []
  },
  getters: {
    productDetails: (state) => (index) => { 
        return state.allProducts[index];
    },
    allProducts(state) {
      return state.products
    }
  },
  mutations: {
    setProducts(state, products) {
      state.allProducts = products
    }
  },
  actions: {
    
  },
  modules: {
  }
})
