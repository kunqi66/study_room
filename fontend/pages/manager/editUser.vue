<template>
	<view>
		<uni-table ref="table" emptyText="暂无更多数据" @selection-change="selectionChange">
			<uni-tr>
				<uni-th width="100" aling="center">姓名</uni-th>
				<uni-th width="100" aling="center">学号</uni-th>
				<uni-th width="100" aling="center">电话</uni-th>
				<uni-th width="160" align="center">选项</uni-th>
				<uni-th width="160" align="center">操作</uni-th>
			</uni-tr>
			<uni-tr v-for="(item,index) in editUser" :key="index">
				<uni-td align="center">{{ editUser[index].name }}</uni-td>
				<uni-td align="center">{{ editUser[index].student_number }}</uni-td>
				<uni-td align="center">{{ editUser[index].number }}</uni-td>
				<uni-td>
					<button class="uni-button" v-if="item.illegal_number<=15" size="mini" type="primary">可用</button>
					<button v-else>不可用</button>
				</uni-td>
				<uni-td>
					<view class="uni-group">
						<button class="uni-button" size="mini" type="primary" @click="edit()">修改</button>
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
				editUser:[],
				loading: false
			}
		},
		onLoad() {
			var that=this
			uni.request({
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				url:getApp().globalData.urlRoot+"manager/loadUser",
				method:'POST',
				data:{
				},
				success: (res) => {
					if(res.data.suc){
						console.log("获取用户列表成功")
						that.editUser=res.data.form
						console.log(that.editUser[0].name)
						console.log(res.data.form)
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
			edit(){
				var that=this
				uni.request({
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"manager/editUser",
					method:'POST',
					data:{
						number:30,
					},
					success: (res) => {
						if(res.data.suc){
							console.log("修改成功")
							
						}else{
							console.log("修改失败")
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
			}
		}
	}
</script>

<style>

</style>