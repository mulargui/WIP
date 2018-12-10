import java.sql.Timestamp;
import java.time.Instant;
import java.util.List;

public class MasterSeed {
    public final static int MAX_NAME_LENGTH = 20000;
    public final static int MAX_TEXT_LENGTH = 100000;
    public final static int MAX_URL_LENGTH = 2083;

    //private long id;
    // length=MAX_NAME_LENGTH
    private String title;
    // length=MAX_TEXT_LENGTH
    private String description;
    private String postedBy;
    private Long userId;
    private String startDate;
    private Timestamp created;
    private Long modified;
    private Long expires;
    private String longitude;
    private String latitude;
	// length=MAX_URL_LENGTH)
    private String logoUrl;
    private Long deletedDate;
    //private Category category;
    private String sourceId;
    private String sourceUpdatedAt;
    private Long eventStartUtc;
    private String eventEndUtc;
    private String url;
    //private EventSource source;
    private Timestamp updatedAt;
	
	boolean equals (MasterSeed ms)
	{
		//if both events have the same URL, they are the same event
		if (url.equals(ms.url)) return true;
		return false
	}
}
