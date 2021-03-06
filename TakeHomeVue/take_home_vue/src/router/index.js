// 配置路由相关的信息
import VueRouter from 'vue-router';
import Vue from 'vue';
// 1.通过Vue.use(插件), 安装插件
Vue.use(VueRouter)
// 2.创建VueRouter对象
const routes = [
  {
    path: '/',
    name:"helloWorld",
    // redirect重定向
    redirect: '/upload_img',
  },
  {
    path: '/upload_img',
    name: 'upload_img',
    component: () => import('@/views/upload_img.vue')
  }
]
const router = new VueRouter({
  // 配置路由和组件之间的应用关系
  routes: routes,
  mode: 'history',
  linkActiveClass: 'active'
})
// 3.将router对象传入到Vue实例
export default router