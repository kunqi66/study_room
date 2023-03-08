<template>
	<view>
		<view>
			<view  class="card_home1" v-for="(item,index) in list">
				<view :class="index/2==0?'right':'left'">
					<uni-card :title="item.title" :isFull="true" @click="onclick(index)">
						<text class="text_home" >自习室还剩余：{{item.number}}个座位</text>
					</uni-card>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list:[{},{},{},{},{},{}],
			}
		},
		onLoad() {
			var that=this;
			uni.request({
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"manager/loadRoom",
					method:'POST',
					data:{
					},
					success: (res) => {
						if(res.data.suc){
							console.log("获取管理员列表成功")
							that.list=res.data.form
							console.log(that.list[0].title)
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
			onclick(index){
				console.log("点击了")
			}
		}
	}
</script>

<style>
	.text_home{
		color: crimson;
	}
	
	.left{
		border-radius: 10px 10px 10px 10px;
		margin-left: 5%;
		width: 40%;
		float: left;
		margin-top: 50px;
	}
	.right{
		width: 40%;
		margin-left: 5%;
		margin-right: 5%;
		float: right;
		margin-top: 50px;
	}
</style>
