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
	
	
    private String url;
    // length=MAX_NAME_LENGTH
    private String title;
    private String longitude;
    private String latitude;
    private String startDate;
    private Long eventStartUtc;
    private String eventEndUtc;
    // length=MAX_TEXT_LENGTH
    private String description;
	
	boolean equals (MasterSeed ms)
	{
		static long SIMILAR_TIME = 20000;
		static float SIMILAR_LAT = 0.0009; //roughly 100 meters
		static float SIMILAR_LONG = 0.0012; //roughly 100 meters
		
		float fLongitude = float (longitude);
		float fLatitude = float (latitude);
		float mfLatitude = float (ms.latitude);
		float mfLongitude = float (ms.longitude);
		
		boolean sameUrl = url.equals(ms.url);
		boolean sameTitle = title.equals(ms.title);
		boolean samePlace = fLongitude == mfLongitude && fLatitude == mfLatitude;
		boolean closePlace = (abs(fLatitude - mfLatitude) < SIMILAR_LAT) && (abs(flongitude - mflongitude) < SIMILAR_LONG);
		boolean sameStartTime = eventStartUtc == ms.eventStartUtc;
		boolean closeStartTime = abs(eventStartUtc - ms.eventStartUtc) < SIMILAR_TIME;
		
		//if both events have the same URL, they are the same event
		if (sameUrl) return true;
		if(sameTitle && samePlace && sameStartTime) return true;
		if(sameTitle && closePlace && closeStartTime) return true;
		return false;
	}
}
