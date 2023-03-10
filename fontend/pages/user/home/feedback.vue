<template>
	<view>
		<uni-section>
					<view class="example">
						<view class="title">
							<uni-title type="h1" title="投诉" align="center" color="#1aad19"></uni-title>
						</view>
						<view style="margin-top: 30px;">
							<uni-forms ref="customForm" :rules="customRules" :modelValue="customFormData">
												<uni-forms-item label="自习室选择" required>
													<uni-data-checkbox v-model="customFormData.room" :localdata="rooms" />
												</uni-forms-item>
												<uni-forms-item label="座位选择" required>
													<uni-easyinput v-model="customFormData.num" placeholder="请输入座位号" />
												</uni-forms-item>
												<uni-forms-item label="投诉原因" required>
													<uni-data-checkbox v-model="customFormData.Reason" multiple :localdata="Reasons" />
												</uni-forms-item>
												<view class="example-body">
													<uni-datetime-picker type="date" :clear-icon="false" v-model="customFormData.datetimesingle" @maskClick="maskClick" />
												</view>
											</uni-forms>
						</view>
						<view style="margin-top: 50px;">   
							<button type="primary" plain="true" style="width: 50%;" @click="submit()">提交</button>
						</view>
						
					</view>         
				</uni-section>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				customFormData: {
									room: 2,
									num:1,
									Reason: [5],
									otherReason: '',
									datetimesingle: 1627529992399
								},
								rooms: [{
													text: '1号',
													value: 1
												}, {
													text: '2号',
													value: 2
												}, {
													text: '3号',
													value: 3
												},{
													text: '4号',
													value: 4
												},{
													text: '5号',
													value: 5
												},{
													text: '6号',
													value: 6
												}
												],
												// 多选数据源
								Reasons: [{
													text: '大声喧哗',
													value: 1
												}, {
													text: '乱扔垃圾',
													value: 2
												}, {
													text: '乱占座位',
													value: 3
												}, {
													text: '桌面涂鸦',
													value: 4
												}, {
													text: '情侣亲热',
													value: 5
												}, {
													text: '其他',
													value: 6
												}],
								
				
			}
		},
		methods: {
			submit(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/submitComp",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
							"room": this.customFormData.room,
							"site": this.customFormData.num,
							"reason": this.customFormData.Reason,
							"time":this.customFormData.datetimesingle,
						},
					method:"POST",
					success: (res) => {
						if (res.data.suc) {
							console.log('正常返回')
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}else{
							console.log("上传失败")
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}
					},
				})
			}
		}
	}
</script>

<style>
	.example{
		margin: 20px;
	}
	
.title{
	top: 20px;
	bottom: 30px;
	z-index:-1000;
}
</style>
