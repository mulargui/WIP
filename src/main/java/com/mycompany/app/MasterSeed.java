package com.mycompany.app;

import java.sql.Timestamp;
import java.time.Instant;
import java.util.List;

public class MasterSeed {
    public final static int MAX_NAME_LENGTH = 20000;
    public final static int MAX_TEXT_LENGTH = 100000;
    public final static int MAX_URL_LENGTH = 2083;

	// not useful attributes for comparison
    //private long id;
	// length=MAX_URL_LENGTH)
    private String logoUrl;
    private String postedBy;
    private Long userId;
    private Long modified;
    private Long expires;
    private Long deletedDate;
    //private Category category;
    private String sourceId;
    private String sourceUpdatedAt;
    //private EventSource source;
    private Timestamp updatedAt;
    private Timestamp created;
	
	
    // length=MAX_NAME_LENGTH
    private String title;
    // length=MAX_TEXT_LENGTH
    private String description;
    private String startDate;
    private String longitude;
    private String latitude;
    private Long eventStartUtc;
    private String eventEndUtc;
    private String url;
	
	boolean equals (MasterSeed ms)
	{
		boolean sameurl = url.equals(ms.url);
		boolean sametitle = title.equals(ms.title);
		
		//if both events have the same URL, they are the same event
		if (url.equals(ms.url)) return true;
		return false;
	}
}
