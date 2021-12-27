import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import Dashboard from '../views/Dashboard.vue'
import Admin from '../views/Admin.vue'
import Sale from '../views/Sale-Reporting.vue'
import Cart from '../views/Cart.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/admin',
    name: "Administration",
    component: Admin
  },
  {
    path: '/sale-report',
    name: "Sale Reporting",
    component: Sale
  },
  {
    path: '/cart',
    name: "Cart",
    component: Cart
  }
]

const router = new VueRouter({
  routes
})

export default router
