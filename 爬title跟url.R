#爬標題及網址
LINK<-read.csv("/Users/brenda/Desktop/FRED.csv") #這邊比較麻煩 你需要把最底部分類的網址貼上來，我是存成csv讓他讀
LINKS<-as.character(LINK[,1])
l<-length(LINKS)
doc<-c()
titles<-c()
urls<-c()
i<-1
while(i < l+1){
  doc<-read_html(LINKS[i])
  t<- doc %>%html_nodes(".pager-series-title-gtm") %>% html_text()
  u <- doc %>%html_nodes(".pager-series-title-gtm") %>% html_attr("href")
  titles<-c(titles,t)
  urls<-c(urls,u)
  Sys.sleep(2)
  i<-i+1
}
urls<-paste("https://fred.stlouisfed.org",urls,sep = "")
Tables <- data.frame(Title=titles,Url=urls)
write.csv(Tables, "/Users/brenda/Desktop/Links.csv") #這個輸出的csv你自己設定儲存位置