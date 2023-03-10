<template>
	<view>
		<uni-section title="编辑公告:" type="line"></uni-section>
				<uni-table ref="table" :loading="loading" border stripe emptyText="加载中" @selection-change="selectionChange">
	                 <uni-tr>
	                 	<uni-th width="50" align="center">标题</uni-th>
	                 	<uni-th width="200" align="center">内容</uni-th>
	                 	<uni-th align="center">日期</uni-th>
						<uni-th align="center">选项</uni-th>
	                 </uni-tr>
					<uni-tr v-for="(item, index) in combDate" :key="index">
						<uni-td align="center">{{ combDate[index].notice_title }}</uni-td>
						<uni-td align="center">{{ combDate[index].notice_text }}</uni-td>
						<uni-td align="center">{{ combDate[index].notice_time }}</uni-td>
						<uni-td align="center">
							<button type="primary" size="mini" @click="open(index)"> 编辑 </button>
						</uni-td>
					</uni-tr>
					</uni-table>
					
					
					<uni-popup ref="editData">
						<uni-forms ref="form" :modelValue="formData" >
					<uni-forms-item label="标题" name="title">
							<uni-easyinput  type="text" v-model="formData.notice_title" >
							</uni-easyinput>
						</uni-forms-item>
						<uni-forms-item label="内容" name="text">
							<uni-easyinput type="text" v-model="formData.notice_text" >
							</uni-easyinput>
						</uni-forms-item>
						<uni-forms-item label="日期" name="date">
							<uni-easyinput  type="text" v-model="formData.notice_time" >
							</uni-easyinput>
						</uni-forms-item>
					</uni-forms>
						<view style="display: flex; margin-left: 10upx;">
						<button class="but" type="primary" @click="SubmitEdit()">修改</button>
						</view>
						</uni-popup>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				formData:{},
				combDate:[],
				editData:false,
				editid:-1,
			}
		
		
	},
	onLoad() {
		var that=this
		uni.request({
			header: { 'content-type':'application/x-www-form-urlencoded'},
			url:getApp().globalData.urlRoot+"manager/loadNotice",
			method:'POST',
			data:{
				
			},
			success: (res) => {
						if(res.data.suc){
							that.combDate=res.data.form
							console.log(that.combDate[0].title)
							console.log(that.combDate)
						}else{
							console.log(res.data.message)
						}
					},
					fail() {
						uni.showToast({
							title: "错误！",
							icon: 'none'
						})
					}
				})
			},
			   methods: {
				open(index){
					this.editid=index+1
					console.log(this.editid)
					this.formData=this.combDate[index]
					this.$refs.editData.open();
				},
				   
			   	SubmitEdit(){
			   		var that=this;
			   		uni.request({
			   			url:getApp().globalData.urlRoot+"manager/SYGG",
						header: {'Authorization':getApp().globalData.token,
						   'content-type':'application/x-www-form-urlencoded'},
						   data:{
						   	"title":that.formData.notice_title,
							"text":that.formData.notice_text,
							"date":that.formData.notice_time,
							"editid":that.editid
						   },
						   method:"POST",
						   		success(res) {
						   			if(res.data.suc){
						   				uni.showToast({
						   					title: String(res.data.message),
						   					icon: 'checkmarkempty'
						   				})
						   				uni.navigateTo({
						   					url: "/pages/manager/SYGG",
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
						   },
						   
						}
			   }
</script>

<style>

</style>