trigger OnAccount on Account (after insert, after update, before delete) 
{
    Triggers__c triggerAccount = Triggers__c.getInstance('Account.CreateDocumentPlaceHolder');
    if(triggerAccount != null && triggerAccount.Active__c == true && Trigger.isAfter && Trigger.isInsert)
        AccountTriggers.CreateDocumentPlaceHolder();
        
    triggerAccount = Triggers__c.getInstance('Account.DelDocumentsWhenAccDeleted');
    if(triggerAccount != null && triggerAccount.Active__c == true)
        AccountTriggers.DeleteRelatedChildRecordsWhenAccDeleted();      
}