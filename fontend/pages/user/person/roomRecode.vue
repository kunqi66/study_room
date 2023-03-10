<template>
	<view>
		<uni-table ref="table" :loading="loading" border stripe emptyText="暂无更多数据" @selection-change="selectionChange">
						<uni-tr>
							<uni-th width="200" align="center">时间</uni-th>
							<uni-th align="center">自习室号</uni-th>
							<uni-th width="204" align="center">座位号</uni-th>
						</uni-tr>
						<uni-tr v-for="(item, index) in tabalDate" :key="index">
							<uni-td align="center">{{ tabalDate[index].start }} -- {{ tabalDate[index].end }}</uni-td>
							<uni-td align="center">{{ tabalDate[index].class_number }}</uni-td>
							<uni-td>
								{{ tabalDate[index].site_number }}
							</uni-td>
						</uni-tr>
					</uni-table>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tabalData:[],
			}
		},
		onLoad(){
			var that=this
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"manager/loadRecord",
				method:'POST',
				data:{
				},
				success: (res) => {
					if(res.data.suc){
						console.log("获取管理员列表成功")
						that.tabalDate=res.data.form
						console.log(res.data.form)
						console.log(that.tabalDate[0].name)
						console.log(that.tabalData)
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
			
		}
	}
</script>

<style>

</style>
