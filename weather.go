package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/gocolly/colly"
)

type Weather_Report struct {
	Day     string
	High    string
	Low     string
	Weather string
	Percip  string
	Wind    string
}

var Country string
var Region string
var City string
var Weather_Code string

func main() {
	c := colly.NewCollector()
	Report := make([]Weather_Report, 0)
	c.OnHTML("div[data-testid=DetailsSummary]", func(e *colly.HTMLElement) {
		item := Weather_Report{}
		//item.Name = e.Text
		item.Day = e.ChildText("h3[data-testid=daypartName]")
		item.High = e.ChildText("span[class=DetailsSummary--highTempValue--3Oteu]")
		item.Low = e.ChildText("span[class=DetailsSummary--lowTempValue--3H-7I]")
		item.Weather = e.ChildText("span[class=DetailsSummary--extendedData--365A_]")
		item.Percip = e.ChildText("span[data-testid=PercentageValue]")
		item.Wind = e.ChildText("span[data-testid=Wind]")
		Report = append(Report, item)

	})

	c.OnError(func(r *colly.Response, e error) {
		fmt.Println("Got this error:", e)
	})

	d := colly.NewCollector()
	d.OnHTML("tbody", func(f *colly.HTMLElement) {
		EHA := f.ChildText("tr > td")
		OK := strings.Split(EHA, "...")
		LAST := strings.Split(OK[1], "ZIP")
		ACTUAL_LAST := strings.Split(LAST[0], "Country")
		New_VALUE := strings.Split(ACTUAL_LAST[1], "Region")
		OK_VALUE := strings.Split(New_VALUE[1], "City")
		Country = strings.ToLower(New_VALUE[0])
		Region = OK_VALUE[0]
		City = OK_VALUE[1]
	})

	e := colly.NewCollector()
	e.OnHTML("div[class=country__codes]", func(f *colly.HTMLElement) {
		Stripping_Time := strings.Split(f.Text, City)
		if len(Stripping_Time) == 1 {
			println("City ", City, " Not Found")
			return
		}

		fmt.Println(City)
		New_Time := strings.Split(Stripping_Time[1], " ")
		Weather_Code = New_Time[2]

	})

	d.Visit("https://www.showmyip.com/")

	left := "https://weather.codes/"

	if Country == "united states" {
		Country = "united-states-of-america/"
		Region = strings.ToLower(Region)
		Country = Country + Region
	}

	e.Visit(strings.TrimSpace(left + Country))

	site := "https://weather.com/weather/tenday/l/"
	Weather_Code = strings.TrimSpace(Weather_Code)
	fmt.Println(Weather_Code)

	c.OnScraped(func(r *colly.Response) {
		js, err := json.MarshalIndent(Report, "", "    ")
		if err != nil {
			log.Fatal(err)
		}
		new_fjson := ".json"
		slash := "/"
		if strings.Contains(Country, slash) {
			Country = strings.Replace(Country, slash, ",", -1)
		}
		comma := ","
		fmt.Println(Country)
		if err := os.WriteFile(City+comma+Country+new_fjson, js, 0664); err == nil {
			fmt.Println("Data written to file successfully")
		}
	})
	c.Visit(site + Weather_Code)
}
