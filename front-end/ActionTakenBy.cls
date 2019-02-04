public with sharing class ActionTakenBy {
	
	public static String ConvertToJSON(Decision__c[] decisions){
		List<ActionTakenBy> approvers = new List<ActionTakenBy>();
		for(Decision__c dec : decisions){
			approvers.add(new ActionTakenBy(dec));
		} 
		return JSON.serialize(approvers);
	}
	
	public static String ConvertToJSON(String strRole, String strAction, String strDecisionId){
		List<ActionTakenBy> approvers = new List<ActionTakenBy>();
		ActionTakenBy actionTakenBy = new ActionTakenBy(strRole, strAction, strDecisionId);
		approvers.add(actionTakenBy);
		return JSON.serialize(approvers);
	}

	public ActionTakenBy(String strRole, String strAction, String strDecisionId) {
		role = strRole;
		action = strAction;
		name = Userinfo.getName();
		memberid = UserInfo.getUserId();
		id = strDecisionId;
	}
	public ActionTakenBy(Decision__c dec) {
		role = dec.Role__c;
		name = dec.Decision_By__r.Name;
		memberid = dec.Decision_By__c;
		action = dec.Decision__c;
		id = dec.Id;
	}
	public String role {get;set;}
	public String name {get;set;}
	public String memberid {get;set;}
	public String action {get;set;}
	public String id {get;set;}
}