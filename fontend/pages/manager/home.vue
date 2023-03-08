<template>
	<view>
		<view style="margin-left: 45rpx;color: orange;margin-top: 30rpx;font-size: 20px;">
			<text>管理员选项</text>
		</view>
		
		<view class="card-home">
			<view style="margin-left: 20rpx;margin-bottom: 10rpx; font-size: 15px;">
				<text>用户管理</text>
			</view>
			<uni-card>
				<uni-list style=" border-radius: 18rpx;">
					<view style="border-radius: 18rpx;">
					<uni-list-item title="更改用户权限" link to="/pages/Manager/editUser" @click="onClick($event,1)"></uni-list-item>
					</view>
					<view>
						<uni-list-item title="更改座位信息" link to="/pages/Manager/editSource" @click="onClick($event,1)"></uni-list-item>
					</view>
					<view>
						<uni-list-item title="投诉信息处理" link to="/pages/manager/complaint" ></uni-list-item>
					</view>
				</uni-list>
			</uni-card>
		</view>
		
		<view class="card-home">
			<view style="margin-left: 20rpx;margin-bottom: 10rpx;font-size: 15px;">
				<text>资源管理</text>
			</view>
			<uni-card>
				<uni-list style=" border-radius: 18rpx;"> 
					<view style="border-radius: 18rpx;">
					<uni-list-item title="新增公告"  link to="/pages/manager/createNotice"></uni-list-item>
					</view>
					<view>
					<uni-list-item title="编辑公告" link to="/pages/manager/createMana"></uni-list-item>
					</view>
				</uni-list>
			</uni-card>
		</view>
		<view style="margin: 30px;">
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			onclick(u){
				uni.navigateTo({
					url: u
				})
			},
		}
	}
</script>

<style>
	.card-home{
		margin-top: 40px;
	}
	.item_button{
		width: 100%;
		height: 15px;
	}
</style>
