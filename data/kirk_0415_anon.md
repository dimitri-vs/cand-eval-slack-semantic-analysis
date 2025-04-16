CONTEXT:
- David Sodaman: Agency owner/founder
- Clay Bell: Agency accounts/project manager
- Kaelen H and Axel R: Agency developers
- Vin D & Richard R: Clients of the agency

--- --- ---

**Vin D. - 2025-04-02 17:05:14**

Hi guys @ClayBell @KaelenH. @AxelR. do we have any updates on how the pilot is looking? Or need anything from me or @RichardR.?

---

**Axel R. - 2025-04-02 17:09:01**

@VinD. broad update so far is that:
• I have extracted structured data from all <REDACTED> Deals (281 excel files) in form or JSON files of Print-Overview and Print-I&amp;E sheets.
• Print-Overview sheet's AI driven data extraction is complete.
• Print-I&amp;E data extraction has some gaps that I am working on. The sheet has data in non-consistant manner and hence taking a bit longer than Print-Overview.
Immediate next steps (in next 1-2 days):
• Complete data extraction of Print-I&amp;E
• Seed all extracted data in a database
• Expose this as queryable via a chat prompt.


---

**Axel R. - 2025-04-02 17:10:26**

For the first phase, I am not parsing data from PRINT-Lease Trend tab. Will get back to it once the above steps are complete.

---

**Axel R. - 2025-04-02 19:01:52**

@VinD. within the Print-I&amp;E tabs, for each period, are Actual and Adjusted tabs both important, or only one specific of these is needed?

---

**Vin D. - 2025-04-02 19:12:55**

Thanks for the update @AxelR.. For now, just focus on the Actual column. We may need to build in functionality later for both, but I think the actual column is the best place to start.

@RichardR. do you think that is the right approach?

---

**Richard R. - 2025-04-02 21:19:27**

Yes, let's just focus on actual for the test version and we can include adjusted later if we decide we want that

---

**Axel R. - 2025-04-03 11:44:57**

@VinD. with reference to a typical sample of `PRINT-I&amp;E` sheet (as attached), I understand that the 'Actual' column along with all the row labels and data is most important for now. However, there is Adjusted &gt; Dec-20 T3 column as well. In this context of T&lt;Period&gt; being important for querying data, can you help me with these clarifications:
• Should it only be the Actual column that we fetch?
• Is the year in column header (2020 in this case) important for any immediate queries?
• One of the column header is Dec-20 T3. Most files have such headers. Is this column relevant as it has T&lt;Period&gt;? If yes, are we interested only in the T3 part or need Dec-20 part as well?

---

**Richard R. - 2025-04-04 01:09:14**

• For the first version, only fetch the Actual column
• Yes, the header will be important to be able to query. The format on most of the summaries will be mmm-yy T12, for example, Jan-25 T12. This represents the last 12 months from Jan-25 through Feb-24. So a potential query may be "what is the average insurance expense since 2024?"
• The actual column will almost always be in the mmm-yy T12 format and the main point of that data is the date part
@AxelR.

---

**Axel R. - 2025-04-05 07:26:33**

Hey @VinD. here's a broad update on the pilot project so far:
• We have extracted structured data from all <REDACTED> Deals (281 excel files) from Print-Overview and Print-I&amp;E sheets; parsed data and seeded it in the database
• The database is accessible using:
    ◦ An analytics dashboard and;
    ◦ A chat prompt for answering questions and drawing ad-hoc insights
This is accessible via this link- <REDACTED_URL> (default demo credentials are: Username: <REDACTED> Password: <REDACTED>). You can start exploring it and provide feedback on any enhancements needed or any other issues that you observe.

Plan for upcoming week is as follows:
• Add BD data and other relevant details from the PRINT-Lease sheet - so that more insights can be drawn and more questions can be answered.
• Add remaining data of Ohio Deals


#### Thread replies:

**Axel R.** - 2025-04-09 06:25:29

Hey @RichardR. did you get a chance to review this

---

**Axel R. - 2025-04-05 07:28:33**

Note that in the above context questions such as these will not work as expected:
• What is the average in place rent for 2 BD units in Austin? $ amount and as PSF please
• Show me a map of the deals we've underwritten in Austin with their names, occupancy, average in place rents and average asking rents listed.
Questions related to BD will be supported when we ingest data from PRINT-Lease sheet and, in case of maps, we will get back to you separately.

---

**Richard R. - 2025-04-07 13:31:33**

Thanks for the update, I will look through and provide any comments.

Update on our end- Vin D. has taken a new role and his last day with us was on Friday. I will be the primary contact for this project moving forward.

---

**Axel R. - 2025-04-10 16:42:22**

Hey @RichardR. as planned, we have now:
• Added data from 'PRINT-Lease Trend' sheet and hence the chat will now support queries with type of properties too, like 'What is the average in place rent for 2 BD units in Austin?'
• Add remaining data of Ohio Deals, so the questions can also cover cities in Ohio now.
Please review it via this link link- <REDACTED_URL> (default demo credentials are: Username: <REDACTED> Password: <REDACTED>d) and provide feedback on any enhancements needed or any other issues that you observe.

---

**Richard R. - 2025-04-11 15:33:34**

Thanks. Are you able to see different chats that I have done? If i encounter things I would have done differently is the program in a place that it can be trained? Or is this strictly a test environment?
• Overall, I love the chat functionality
• The speed on some queries is slower. In a full, live version would the speed be any different?
• Some questions it seems to be making calculations different than how we would want it done or referencing information that we would do different. What is the best way to go about that? Tell you or start to tell the system?

---

**Richard R. - 2025-04-11 15:38:50**

Example screenshot from the chat. In this case I am asking what the average Loss to Lease is from the income section of the financial analysis. It seems the model is doing a calculation based on in-place and asking rent which I dont want it to do

---

**Richard R. - 2025-04-11 15:42:01**

The expenses seem to be working great. I am having trouble asking income related questions from the I&amp;E section of our underwriting. Is this data in the system?

---

**Axel R. - 2025-04-12 11:08:05**

Hey @RichardR. thanks for taking time to review the work so far and here's to answer your questions:

• Are you able to see different chats that I have done?
    ◦ The chats history is not retained after logout, so I would not be able to review all past chats. It's recommended that you screenshot chats that you see an issue with so that we can iterate and train the model in the expected way.
• If i encounter things I would have done differently is the program in a place that it can be trained?
    ◦ Yes, we can train the model differently based on the observations that you see.
• The speed on some queries is slower. In a full, live version would the speed be any different?
    ◦ The speed will pretty much be the same in the live version as well. This is because of the way the system works. Basically, all excel sheets are parsed, and the extracted data is stored in a database. Each chat question, creates a dynamic query to this database and retrieves the data on the fly to reply to your chat. Hence the UI says 'thinking...' while all this processing is ongoing and will take similar time in production.
• The expenses seem to be working great. I am having trouble asking income related questions from the I&amp;E section of our underwriting. Is this data in the system?
    ◦ All the data is in place, but this is happening because the income section is very thinly spread in term of income headings. Many headings barely have been used only in a few properties and hence the model was not trained to query those ('bad debt' being one such). While we have all data, but currently the model is actively trained only to query on high frequency usage based income items (which are at least used in more than 20% of properties) which include these. We can add more to this list based on use cases, but making all income heads queryable is not doable due to the way the data is structured as it has about 475 unique income heads, some barely used in 1-2 properties. For now will add bad debt to the list.
        ▪︎ - income["Plus: Admin &amp; Application Fee"] (number)
        ▪︎ - income["Plus: Application Fee"] (number)
        ▪︎ - income["Plus: Late Fee"] (number)
        ▪︎ - income["Plus: Other Income"] (number)
        ▪︎ - income["Plus: Pet Fee"] (number)
        ▪︎ - income["Plus: RUBS (Water/Sewer)"] (number)
        ▪︎ - income["Scheduled Rent"] (number)
        ▪︎ - income["Gross Potential Rent"] (number)
        ▪︎ - income["Net Rental Income"] (number)
        ▪︎ - income["Effective Gross Income"] (number)
        ▪︎ - income["Period"] (ISO datetime string)
        ▪︎ - income["PeriodT"] (string)
• I am asking what the average Loss to Lease is from the income section of the financial analysis. It seems the model is doing a calculation based on in-place and asking rent which I dont want it to do.
    ◦ Being an all AI model, it will typically use generally accepted formulas for such cases. If you see any such occurrences, give us a heads up and we will explicitly embed certain formulas into the model.


---

**Axel R. - 2025-04-12 11:18:01**

Based on the above, here's my recommended way forward:

• Based on your inputs we will train the model for specific things flagged such as:
    ◦ including of bad debt in income
    ◦ addition of any other income components that you commonly use, yet does not appear in the list provided
    ◦ specific formulas such as average Loss to Lease (please help with calculation of this)
• I suggest that you go through the 'Dashboard' as well. This is basically a space where we can pre-create some reports. You can suggest some report views that are most commonly used for decision making so that we can configure these. The benefit of Dashboards over chat is that these are directly created using data from the database (without any AI in between) and hence are quite fast and also will not incur any cost of queries as no LLM tokens are effectively used here.

---

**Richard R. - 2025-04-14 20:45:15**

Attached are notes and examples from when I was testing it earlier today. Please let me know if you have any questions about these.

#### Thread replies:

**Axel R.** - 2025-04-15 07:47:12

Noted. Will incorporate these inputs in training data.

**Axel R.** - 2025-04-15 07:48:22

Also, as suggested earlier, please go through the 'Dashboard' as well. This is basically a space where we can pre-create some reports. You can suggest some report views that are most commonly used for decision making so that we can configure these. The benefit of Dashboards over chat is that these are directly created using data from the database (without any AI in between) and hence are quite fast and also will not incur any cost of queries as no LLM tokens are effectively used here.

---

**Axel R. - 2025-04-15 07:48:22**

Also, as suggested earlier, please go through the 'Dashboard' as well. This is basically a space where we can pre-create some reports. You can suggest some report views that are most commonly used for decision making so that we can configure these. The benefit of Dashboards over chat is that these are directly created using data from the database (without any AI in between) and hence are quite fast and also will not incur any cost of queries as no LLM tokens are effectively used here.

---

**Axel R. - 2025-04-15 14:18:51**

From the perspective of training the mode, this is a rule superset that I am providing:
```Here are some instructions for common calculations:
 - Average of any income line item is the sum of the income line item divided by the sum of the "Gross Potential Rent"; unless otherwise specified.
 - Other income refers to the sum of all income sources that start with "Plus".
 - All average per unit calculations (income, expenses, etc.) should be based on simple division of the sum of the values by the number of units; unless otherwise specified.
 - When calculating average expense or income for specific line items do not want the properties with $0 / null / undefined to be included in the average.; unless otherwise specified.```
Let me know if these sound right, and are in alignment with the observations cited in the doc

---

**Richard R. - 2025-04-15 14:58:25**

ave these rules been implemented? I will test if so