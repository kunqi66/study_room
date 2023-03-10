<template>
	<view :style="{background: 'url('+imageURL+')'}">
		<image src="../../../static/beijing1.jpg"></image>
		<view>
			<view  class="card_home1" v-for="(item,index) in list">
				<view :class="index%2==0?'left':'right'">
					<uni-card :title="item.title" :isFull="true" @click="onclick(index)">
						<text class="text_home" >自习室还剩余：{{item.number}}个座位</text>
					</uni-card>
				</view>
			</view>
		</view>
		
		<uni-popup ref="site1">
			<view v-for="(item,index) in sitelist" v-if="index<10" :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)" > 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-else> 座位已被借用 </button>
				
			</view>
		</uni-popup>
		
		<uni-popup ref="site2">
			<view v-for="(item,index) in sitelist" v-if="9<index&&index<20"   :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-else> 座位已被借用 </button>
			</view>
		</uni-popup>
		
		<uni-popup ref="site5">
			<view v-for="(item,index) in sitelist" v-if="39<index&&index<50" :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-else> 座位已被借用 </button>
			</view>
		</uni-popup>
		
		
		<uni-popup ref="site3">
			<view v-for="(item,index) in sitelist" v-if="19<index&&index<30" :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-if="item.status=='E'"> 座位已被借用</button>
			</view>
		</uni-popup>
		
		<uni-popup ref="site4">
			<view v-for="(item,index) in sitelist" v-if="29<index&&index<40" :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-if="item.status=='E'"> 座位已被借用 </button>
			</view>
		</uni-popup>
		
		<uni-popup ref="site6">
			<view v-for="(item,index) in sitelist" v-if="49<index&&index<60" :class="index%2==1?'right':'left'">
				<button type="primary" v-if="item.status=='A'" @click="jie(index)"> 座位可用 </button>
				<button type="default" v-else-if="item.status=='W'"> 座位维护禁用 </button>
				<button type="warn" v-if="item.status=='E'"> 座位已被借用 </button>
			</view>
		</uni-popup>
		
		<uni-popup ref="apply" type="bottom">
			<uni-section>
				<view class="button">
					<view class="example-body">
						<uni-datetime-picker type="date" :clear-icon="false" v-model="baseFormData.date" @maskClick="maskClick" />
					</view>
					<button type="default"  @click="shut()">取消</button>
					<button type="primary" @click="submit()">提交</button>
				</view>
			</uni-section>
		</uni-popup>
		
		
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				list:[{},{},{},{},{},{}],
				sitelist:[{},{},{}],
				bro_id:-1,
				baseFormData:{},
				imageURL:"/static/beijing1.jpg",
			}
		},
		onLoad() {
			this.load()
		},
		methods: {
			load(){
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
							uni.request({
									header: {'content-type':'application/x-www-form-urlencoded'},
									url:getApp().globalData.urlRoot+"manager/loadSite",
									method:'POST',
									data:{
									},
									success: (res) => {
										if(res.data.suc){
											console.log("获取管理员列表成功")
											that.sitelist=res.data.form
											console.log(that.sitelist[0].title)
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
						fail() {
							uni.showToast({
								title: "获取失败！",
								icon: 'none'
							})
						}
					})
					
			},
			jie(index){
				console.log("第"+index+"个座位调用")
				this.bro_id=index+1;
				this.open()
			},
			onclick(index){
				if(index==0){
				this.$refs.site1.open();
				}
				if(index==1){
				this.$refs.site2.open();
				}
				if(index==2){
				this.$refs.site3.open();
				}
				if(index==3){
				this.$refs.site4.open();
				}
				if(index==4){
				this.$refs.site5.open();
				}
				if(index==5){
				this.$refs.site6.open();
				}
			},
			open(){
				this.$refs.apply.open()
			},
			shut(){
				this.$refs.apply.close()
			},
			submit(){
				var c_number= Math.floor(this.bro_id/10)+1
				var that=this
				uni.request({
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"user/broSite",
					method:'POST',
					data:{
						"c_number":c_number,
						"uid":getApp().globalData.uid,
						"start":that.baseFormData.date,
						"end":"that.baseFormData.end",
						"number":that.bro_id,
					},
					success: (res) => {
						if(res.data.suc){
							console.log("借用座位成功")
							this.load()
							
						}else{
							console.log("借用座位失败")
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
				this.$refs.apply.close();
			}
		}
	}
</script>

<style>
	.beijing1{
		width: 500px;
		height: 80px;
	}
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
