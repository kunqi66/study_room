<template>
	<view>
		<view class="temp">
			<view class="notice_home">
					<uni-title type="h1" title="公告" color="#ffaaa7"></uni-title>
			</view>
			<view class="weather_home" @click="openWeather()">
			
				<view >
				<uni-icons type="contact" size="18"></uni-icons>
				天气：{{ realWeather.info }}
				</view>
				<view>
				<uni-icons type="fire" size="18"></uni-icons>
				温度：{{ realWeather.temperature}} 
				</view>
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				风向：{{ realWeather.direct }} 
				</view>   
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				风力：{{ realWeather.power }}
				</view>

			</view> 
			<view class="manage_home">
				自习室规定：daisikjaksjdlajdlkasjdlskajsakdjaslkdhalksdjlkadjsdfsdfsdfsdf
			</view> 
			<view class="complaint_home">
				投诉写这里
			</view>  
		</view>
			<uni-popup ref="weather" type="center" border-radius="14" width="500px" height="7000px" >
			<view class="tanchuang1">
				<view v-for="(item,index) in weatherList">
					第{{index+1}}天:
					{{ weatherList[index].date }}
					<view>风向:{{weatherList[index].direct}}</view>
					<view>温度:{{weatherList[index].temperature}}</view>
					<view>天气:{{weatherList[index].weather}}</view>
					<view>-----------</view>
				</view>
			</view>
			</uni-popup>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				direct:"",
				weather:{},
				realWeather:{},
				weatherList:[],
			}
		},
		onLoad() {
			this.loadWeather()
			console.log("获取到当前的天气"+this.realWeather+"获取数据"+this.weather)
		},
		methods: {
			openWeather(){
				this.$refs.weather.open()
			},
			loadWeather(){
				var that=this;
				uni.request({
					url:"http://apis.juhe.cn/simpleWeather/query",
					header: {'content-type':'application/x-www-form-urlencoded'},
					method:"GET",
					data:{
						"city":"太原",
						"key":"033d0a7c40bf2b89277303e0f44b08ae",
					},
					success(res) {
						console.log(res);
						that.weather=res.data.result
						that.realWeather=res.data.result.realtime
						that.weatherList=res.data.result.future
						console.log(that.weatherList)
					}
				})
			}
		}
	};
</script>

<style>
	.weather_home{
		width: 45%;
		margin-left: 5%;
		font-size: 18px;
		height: 120px;
		float: left;
	}
	.notice_home{
		width: 90%;
		margin-left: 5%;
		background-color: black;
		margin-bottom: 20px;
	}
	.manage_home{
		background-color: bisque;
		height: 120px;
		width: 45%;
		margin-right: 5%;
		float: right;
	}
	.complaint_home{
		margin-top: 20px;
	}
	.tanchuang1{
		background-color: azure;
		width: 200px;
		height: 530px;
		border-radius: 10px;
		top: 10%;
	}
</style>
