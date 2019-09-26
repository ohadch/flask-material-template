import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './home/HomePage'
import LoginPage from './login/LoginPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/',
      name: 'login',
      component: LoginPage
    },
  ]
})
