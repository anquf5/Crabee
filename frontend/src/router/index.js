import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/company/:id',
    name: 'CompanyDetail',
    component: () => import('../views/CompanyDetail.vue')
  },
  {
    path: '/all_company',
    name: 'all_company',
    component: () => import('../views/CompanyList.vue')},
  {
    path: '/discussion',
    name: 'Discussion',
    component: () => import('../views/Discussion.vue')
  },
  {
    path: '/topic/:id',
    name: 'TopicDetail',
    component: () => import('../views/TopicDetail.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/Signup.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: () => import('../views/MyAccount.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
