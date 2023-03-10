<template>
	<view>
		<uni-table ref="com_table" border stripe emptyText="暂无更多数据">
						<uni-tr>
							<uni-th width="70" align="center">座位号</uni-th>
							<uni-th width="200" align="center">是否可用</uni-th>
							<uni-th width="200" align="center">操作</uni-th>
						</uni-tr>
						<uni-tr v-for="(item, index) in table_data" :key="index">
							<uni-td align="center" class="td">{{ item.id }}</uni-td>
							<uni-td align="center" class="td">
								<button type="primary" size="mini" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
								<button type="default" size="mini" v-else-if="item.status=='W'"> 座位维护禁用 </button>
								<button type="warn" size="mini" v-if="item.status=='E'"> 座位已被借用 </button>
							</uni-td>
							<uni-td>
								<view class="uni-group">
									<button type="primary" size="mini" @click="deal(index,'A')">开放使用</button>
									<button type="warn" size="mini" @click="deal(index,'W')">禁用</button>
								</view>
							</uni-td>
						</uni-tr>
		</uni-table>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				table_data:[],
			}
		},
		onLoad(){
			var that=this
			uni.request({
					header: {'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"manager/loadSite",
					method:'POST',
					data:{
					},
					success: (res) => {
						if(res.data.suc){
							console.log("获取管理员列表成功")
							that.table_data=res.data.form
						}else{
							console.log("未查询到数据")
							console.log(res.data.message)
						}
					},
					fail() {
						uni.showToast({
							title: "获取失败！",
							icon: 'none'
						})
					}
				})
		},
		methods: {
			deal(index,status){
				var c_number= Math.floor((index+1)/10)+1
			
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/dealSite",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
						"id":index+1,
						"c_id":c_number,
						"result":status,
					},       //json
					method:"POST",
					success(res) {
						if(res.data.suc){
							console.log("后端访问成功")
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}else{
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty',
								duration:1500,
							})
						}
					}
				})
			}
		}
	}
</script>

<style>

</style>
