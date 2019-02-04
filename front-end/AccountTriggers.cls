public with sharing class AccountTriggers
{
    public static Map<String, General_Settings__c> mapSettings = Cache.GeneralSettings;
    
    public static void CreateDocumentPlaceHolder()
    {
        SaveResult saveResult = new SaveResult();
        List<Account> lstOrganization = Trigger.new;
        Stage__c newStage = [SELECT Id, Name FROM Stage__c WHERE Object__c = 'Account'];
        system.debug('newStage'+newStage);
        
        if(lstOrganization != null && lstOrganization.size() > 0)
        {
            for(Account account : lstOrganization)
                saveResult = DocumentManager.FireDocumentGeneratorProcess( 'Account', newStage.Id, account);
        }
    }
    
    public static void DeleteRelatedChildRecordsWhenAccDeleted()
    {
        if(Trigger.isBefore && Trigger.isDelete)
        {
            Account AccToBeDeleted = (Account)Trigger.old[0];
            GlobalManager.DeleteRelatedChildRecordsFromParent(AccToBeDeleted,mapSettings.get('RFA.ChildObjects').Value__c);
        }
        
    }
}